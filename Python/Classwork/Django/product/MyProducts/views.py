from django.shortcuts import render,redirect
from MyProducts.models import *

# Create your views here.
def add_product(request):
    return render(request,"product_index.html")

def view_product(request):
    product = products.objects.all()
    return render(request,"pro_display.html",{"products":product})

def register(request):
    data=request.POST
    id = data.get("id")
    p_name = data.get("p_name")
    qty = data.get("qty")
    price = data.get("price")   

    if id:
        pr = products.objects.get(id=id)
        pr.p_name = p_name
        pr.qty = qty
        pr.price = price
        pr.save()
        return render(request,"product_index.html",{"msg":"Products Added"})
    else:
        products.objects.create(p_name = p_name,qty = qty, price = price)
        return render(request,"product_index.html",{"msg":"Products Added"})

def delete_product(request):
    id = request.GET.get("id")
    pr = products.objects.get(id=id)
    pr.delete()
    return redirect("display")

def update_product(request):
    id = request.GET.get("id")
    pr = products.objects.get(id=id)
    return render(request,"product_index.html",{"pr":pr})