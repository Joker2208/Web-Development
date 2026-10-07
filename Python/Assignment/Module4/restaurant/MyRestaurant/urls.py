from django.urls import path
from MyRestaurant.views import *

urlpatterns = [
    path("",index,name="index"),
]