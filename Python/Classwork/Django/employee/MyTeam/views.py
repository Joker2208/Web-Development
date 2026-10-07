from django.shortcuts import render,redirect
from MyTeam.urls import *
from MyTeam.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    employees = Employee.objects.all()
    return render(request,"display.html",{"employees":employees})

def register(request):
    if request.method == "POST":
        data = request.POST
        id = data.get('id')
        name = data.get('name')
        dept = data.get('dept')
        year = data.get('year')

        if id:
            employee = Employee.objects.get(id=id)
            employee.name = name
            employee.dept = dept
            employee.year = year
            employee.save()
            msg = "Employee Updated!"
        else:
            Employee.objects.create(name=name,dept=dept,year=year)
            msg = "Employee Registered!"
    return render(request,"index.html",{"msg":msg})

def delete_emp(request):
    id = request.GET.get("id")
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('display')

def update_emp(request):
    id = request.GET.get("id")
    employee = Employee.objects.get(id=id)
    return render(request,'index.html',{'employee':employee})