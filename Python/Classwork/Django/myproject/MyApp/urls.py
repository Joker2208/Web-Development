from django.urls import path
from MyApp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
]