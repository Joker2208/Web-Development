from django.shortcuts import render, redirect
from MyFood.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def view_list(request):
    foods = Food.objects.all()
    return render(request,"display.html",{"foods":foods})

def register(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        qty = data.get("qty")
        price = data.get("price")

        if id:
            food = Food.objects.get(id = id)
            food.name = name
            food.qty = qty
            food.price = price
            food.save()
            msg = "List Updated!"
        else:
            Food.objects.create(name=name,qty=qty,price=price)
            msg = "Item Added"
    return render(request,'index.html',{"msg":msg})

def delete_item(request):
    id = request.GET.get("id")
    food = Food.objects.get(id = id)
    food.delete()
    return redirect("display")

def update_item(request):
    id = request.GET.get("id")
    food = Food.objects.get(id=id)
    return render(request,'index.html',{"food":food})
