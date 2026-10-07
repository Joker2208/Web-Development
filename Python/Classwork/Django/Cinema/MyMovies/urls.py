from MyMovies.views import *
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",add_movie,name="home"),
    path("register",register,name="register"),
    path('display',view_movies,name="display"),
    path('delete',delete_movies,name="delete"),
    path('update',update_movies,name='update'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)