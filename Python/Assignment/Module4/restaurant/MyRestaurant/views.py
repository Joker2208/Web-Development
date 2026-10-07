from django.shortcuts import render,redirect
from MyRestaurant.models import *
from MyRestaurant.urls import *

# Create your views here.
def index(request):
    return render(request,"index.html")