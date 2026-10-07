from django.urls import path,include
from MyApp.views import *

urlpatterns = [
    path("",user_login,name='login'),
    path("home",home,name='home'),
    path("register",register,name='register'),
    path("logout",user_logout,name='logout'),
]