from django.shortcuts import render, redirect
from MyApp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    students = Students.objects.all()
    return render(request,"display.html",{"students":students})

def register(request):
    if request.method == "POST":
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        course = data.get("course")
        grade = data.get("grade")

        if id:
            student = Students.objects.get(id=id)
            student.name = name
            student.course = course
            student.grade = grade
            student.save()
            msg = "Update Successfull"
        else:
            Students.objects.create(name=name,course=course,grade=grade)
            msg = "Student Registered!"
    return render(request,"index.html",{"msg":msg})

def delete_student(request):
    id = request.GET.get("id")
    student = Students.objects.get(id = id)
    student.delete()
    return redirect('display')

def update_student(request):
    id = request.GET.get("id")
    st = Students.objects.get(id = id)
    return render(request,"index.html",{"st":st})
