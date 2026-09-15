from django.urls import path
from playlists.views import *

urlpatterns = [
    path('',index,name="index"),
    path('music/',home,name="music/")
]
