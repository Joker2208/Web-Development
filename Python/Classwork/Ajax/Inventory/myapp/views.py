from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    print(request.POST)
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        brand = data.get("brand")

        Product.objects.create(name=name,price=price,qty=qty,brand=brand)
        return HttpResponse("Product Registered!!")

def display(request):
    products = Product.objects.all()
    return JsonResponse({"data":list(products.values())})