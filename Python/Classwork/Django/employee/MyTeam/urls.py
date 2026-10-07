from django.urls import path,include
from MyTeam.views import *

urlpatterns = [
    path("",index,name='index'),
    path("display",display,name='display'),
    path('register',register,name='register'),
    path('delete',delete_emp,name='delete'),
    path('update',update_emp,name='update'),
]