from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EnquiryForm
from .models import Category, Jewel

SORTS = {"new": "-created_at", "low": "price", "high": "-price", "name": "name"}


def home(request):
    context = {
        "featured": Jewel.objects.filter(is_featured=True, is_available=True)[:4],
        "categories": Category.objects.all(),
    }
    return render(request, "catalogue/home.html", context)


def catalogue(request):
    jewels = Jewel.objects.filter(is_available=True).select_related("category")
    q = request.GET.get("q", "").strip()
    cat = request.GET.get("category", "")
    material = request.GET.get("material", "")
    sort = request.GET.get("sort", "new")
    if q:
        jewels = jewels.filter(Q(name__icontains=q) | Q(description__icontains=q))
    if cat:
        jewels = jewels.filter(category__slug=cat)
    if material in dict(Jewel.MATERIALS):
        jewels = jewels.filter(material=material)
    jewels = jewels.order_by(SORTS.get(sort, "-created_at"))
    page = Paginator(jewels, 9).get_page(request.GET.get("page"))
    params = request.GET.copy()
    params.pop("page", None)
    context = {"page": page, "categories": Category.objects.all(), "materials": Jewel.MATERIALS,
               "q": q, "cat": cat, "material": material, "sort": sort, "querystring": params.urlencode()}
    return render(request, "catalogue/catalogue.html", context)


def detail(request, slug):
    jewel = get_object_or_404(Jewel.objects.select_related("category"), slug=slug, is_available=True)
    related = Jewel.objects.filter(category=jewel.category, is_available=True).exclude(pk=jewel.pk)[:4]
    return render(request, "catalogue/detail.html", {"jewel": jewel, "related": related})


def about(request):
    return render(request, "catalogue/about.html")


def contact(request):
    initial = {}
    if request.GET.get("jewel", "").isdigit():
        initial["jewel"] = request.GET["jewel"]
    form = EnquiryForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Thank you! Your enquiry has been received and we will get back to you soon.")
        return redirect("contact")
    return render(request, "catalogue/contact.html", {"form": form})
