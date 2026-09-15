from django.shortcuts import render
from MyApp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    data = request.POST
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    Students.objects.create(name=name,email=email,age=age)
    return render(request,"index.html",{"msg":"Registration Successfull"})