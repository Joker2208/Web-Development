from django.shortcuts import render,redirect
from myapp.models import *

def index(request):
    pid = request.GET.get("id")
    product = None
    if pid:
        product = Product.objects.get(id=pid)

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        category = Category.objects.get(id=data.get("category"))

        if product:
            product.name = name
            product.price = price
            product.qty = qty
            product.category = category
            product.save()
            return redirect("display")
        else:
            Product.objects.create(name=name, price=price, qty=qty, category=category)

    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories, "product": product})


def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})

def delete_pro(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("display")


# def update(request):
#     id = request.GET.get("id")
#     product = Product.objects.get(id=id)
#     category = Category.objects.all()
#     return render(request,"index.html",{"product":product, "categories":category})