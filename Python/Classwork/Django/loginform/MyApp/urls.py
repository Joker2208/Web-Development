from django.urls import path 
from MyApp.views import *

urlpatterns = [
    path("",login_user,name="login"),
    path('register',register,name='register'),
    path('home',home,name='home'),
    path('logout',logout_user,name='logout')
]