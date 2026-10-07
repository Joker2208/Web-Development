from django.shortcuts import render, redirect
from MyMovies.models import *
import os

def add_movie(request):
    return render(request, "home.html")

def view_movies(request):
    movies = Cinema.objects.all()
    return render(request, "display.html", {"movies": movies})

def register(request):
    if request.method == "POST":
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        rating = data.get("rating")
        genre = data.get("genre")
        year = data.get("year")
        file =  request.FILES.get("file")

        if id:
            movie = Cinema.objects.get(id = id)
            movie.name = name
            movie.rating = rating
            movie.genre = genre
            movie.year = year

            if file:
                if movie.image:
                    os.remove(movie.image.path)
                movie.image=file
            movie.save()
            msg = "Movie List Updated"
        else:
            Cinema.objects.create(name=name, rating=rating, genre=genre, year=year, image=file)
            msg = "Movie Added"
    return render(request, "home.html", {"msg": msg})

def delete_movies(request):
    id = request.GET.get("id")
    movie = Cinema.objects.get(id = id)
    if movie.image:
        os.remove(movie.image.path)
    movie.delete()
    return redirect("display")

def update_movies(request):
    id = request.GET.get("id")
    movie = Cinema.objects.get(id = id)
    return render(request,"home.html",{"movie":movie})