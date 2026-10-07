from django.urls import path
from MyApp.views import *

urlpatterns = [
    path("",index,name="index"),
    path('display',display,name="display"),
    path('register',register,name='register'),
    path('delete',delete_student,name='delete'),
    path('update',update_student,name='update')
]