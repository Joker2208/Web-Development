from django.urls import path
from MyProducts.views import *

urlpatterns = [
    path('',add_product,name="product"),
    path('register',register,name="register"),
    path('display',view_product,name="display"), 
    path('delete',delete_product,name="delete"),  
    path('update',update_product,name="update")
]