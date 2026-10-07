from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("test",test,name="test"),
    path("countries",countries,name="countries"),
    path("state",states,name="state"),
    path("city",cities,name="city")
]