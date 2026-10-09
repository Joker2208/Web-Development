import csv
from datetime import timedelta

from django.contrib import messages
from django.db import transaction
from django.db.models import DecimalField, ExpressionWrapper, F, Q, Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import CategoryForm, ProductForm, StockMovementForm
from .models import Category, Product, StockTransaction
from .permissions import ADMIN, MANAGER, STAFF, role_required

VALUE = ExpressionWrapper(F("quantity") * F("unit_price"), output_field=DecimalField(max_digits=14, decimal_places=2))


def low_stock_products():
    return Product.objects.filter(quantity__lte=F("reorder_level")).select_related("category")


@role_required(STAFF)
def dashboard(request):
    products = Product.objects.all()
    context = {
        "product_count": products.count(),
        "total_units": products.aggregate(t=Sum("quantity"))["t"] or 0,
        "total_value": products.aggregate(t=Sum(VALUE))["t"] or 0,
        "low_stock": low_stock_products()[:8],
        "low_stock_count": low_stock_products().count(),
        "recent": StockTransaction.objects.select_related("product", "performed_by")[:6],
    }
    return render(request, "inventory/dashboard.html", context)


# ---------- products ----------
@role_required(STAFF)
def product_list(request):
    products = Product.objects.select_related("category")
    q = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")
    low_only = request.GET.get("low") == "1"
    if q:
        products = products.filter(Q(name__icontains=q) | Q(sku__icontains=q))
    if category.isdigit():
        products = products.filter(category_id=category)
    if low_only:
        products = products.filter(quantity__lte=F("reorder_level"))
    context = {"products": products, "categories": Category.objects.all(), "q": q, "category": category, "low_only": low_only}
    return render(request, "inventory/product_list.html", context)


@role_required(MANAGER)
def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        product = form.save()
        messages.success(request, f"Product '{product.name}' created.")
        return redirect("product_list")
    return render(request, "inventory/form.html", {"form": form, "title": "Add product"})


@role_required(MANAGER)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Product '{product.name}' updated.")
        return redirect("product_list")
    return render(request, "inventory/form.html", {"form": form, "title": f"Edit {product.name}"})


@role_required(ADMIN)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        if product.transactions.exists():
            messages.error(request, "This product has stock history and cannot be deleted.")
        else:
            product.delete()
            messages.success(request, f"Product '{product.name}' deleted.")
        return redirect("product_list")
    return render(request, "inventory/confirm_delete.html", {"product": product})


@role_required(MANAGER)
def category_create(request):
    form = CategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Category added.")
        return redirect("product_list")
    return render(request, "inventory/form.html", {"form": form, "title": "Add category"})


# ---------- stock movements ----------
@role_required(STAFF)
def stock_move(request):
    initial = {}
    if request.GET.get("product", "").isdigit():
        initial["product"] = request.GET["product"]
    form = StockMovementForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            # Lock the row and re-check, so two simultaneous requests cannot oversell.
            product = Product.objects.select_for_update().get(pk=form.cleaned_data["product"].pk)
            move = form.save(commit=False)
            if move.movement_type == StockTransaction.OUT:
                if move.quantity > product.quantity:
                    form.add_error(None, f"Only {product.quantity} units of {product.name} in stock.")
                    return render(request, "inventory/form.html", {"form": form, "title": "Record stock movement"})
                product.quantity -= move.quantity
            else:
                product.quantity += move.quantity
            product.save(update_fields=["quantity", "updated_at"])
            move.performed_by = request.user
            move.save()
        messages.success(request, f"{move.get_movement_type_display()}: {move.quantity} x {product.name}. New stock: {product.quantity}.")
        if product.is_low_stock:
            messages.warning(request, f"{product.name} is at or below its reorder level ({product.reorder_level}).")
        return redirect("transaction_list")
    return render(request, "inventory/form.html", {"form": form, "title": "Record stock movement"})


@role_required(STAFF)
def transaction_list(request):
    transactions = StockTransaction.objects.select_related("product", "performed_by")
    kind = request.GET.get("type", "")
    if kind in (StockTransaction.IN, StockTransaction.OUT):
        transactions = transactions.filter(movement_type=kind)
    return render(request, "inventory/transaction_list.html", {"transactions": transactions[:200], "kind": kind})


# ---------- reports ----------
def _report_data():
    since = timezone.now() - timedelta(days=30)
    recent = StockTransaction.objects.filter(created_at__gte=since)
    return {
        "by_category": Category.objects.annotate(units=Sum("products__quantity"), value=Sum(F("products__quantity") * F("products__unit_price"), output_field=DecimalField(max_digits=14, decimal_places=2))),
        "low_stock": low_stock_products(),
        "total_value": Product.objects.aggregate(t=Sum(VALUE))["t"] or 0,
        "in_30": recent.filter(movement_type=StockTransaction.IN).aggregate(t=Sum("quantity"))["t"] or 0,
        "out_30": recent.filter(movement_type=StockTransaction.OUT).aggregate(t=Sum("quantity"))["t"] or 0,
        "generated": timezone.localtime(),
    }


@role_required(MANAGER)
def report(request):
    return render(request, "inventory/report.html", _report_data())


@role_required(MANAGER)
def report_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="stock_report_{timezone.localdate()}.csv"'
    writer = csv.writer(response)
    writer.writerow(["SKU", "Product", "Category", "Quantity", "Reorder level", "Unit price", "Stock value", "Low stock"])
    for p in Product.objects.select_related("category"):
        writer.writerow([p.sku, p.name, p.category.name, p.quantity, p.reorder_level, p.unit_price, p.stock_value, "YES" if p.is_low_stock else "no"])
    return response
