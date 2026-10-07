from django.shortcuts import render,redirect
from MyApp.urls import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        data = request.POST
        uname = data.get('username')
        password = data.get('password')

        user=authenticate(username=uname,password=password)

        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request,"login.html",{'err': "Invalid User"})

    else:
        return render(request,'login.html')

    

def register(request):
    if request.method == 'POST':
        data = request.POST
        fname = data.get('first_name')
        lname = data.get('last_name')
        uname = data.get('username')
        password = data.get('password') 

        if User.objects.filter(username=uname).exists():
            return render(request,'reg.html',{"error":"User Exists!!"})

        User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password)
        return render(request,'reg.html',{'msg':'User Registered!'})

    return render(request,'reg.html')

        
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


def logout_user(request):
    logout(request)
    return redirect('login.html')