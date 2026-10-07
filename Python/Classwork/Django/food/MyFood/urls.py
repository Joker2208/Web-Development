from django.urls import path
from MyFood.views import *

urlpatterns = [
    path("",index,name="index"),
    path('display',view_list,name='display'),
    path('register',register,name='register'),
    path('delete',delete_item,name='delete'),
    path('update',update_item,name='update')
]