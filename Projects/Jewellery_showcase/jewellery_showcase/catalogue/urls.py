from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("collection/", views.catalogue, name="catalogue"),
    path("collection/<slug:slug>/", views.detail, name="detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
