from django.shortcuts import render,redirect
from MyApp.urls import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get('username')
        password = data.get('password')

        user = authenticate(username=uname,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request,"login.html",{'err':"Invalid Credentials"})

    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        data=request.POST
        fname = data.get("fname")
        lname = data.get("lname")
        username = data.get("username")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return render(request,'reg.html',{"err":"User already exists"})

        User.objects.create_user(first_name=fname,last_name=lname,username=username,password=password)
        return render(request,"reg.html",{"msg":"User Registered!"})

    return render(request,'reg.html')

@login_required(login_url="login")
def home(request):
    return render(request,"home.html")

def user_logout(request):
    logout(request)
    return redirect('login')
