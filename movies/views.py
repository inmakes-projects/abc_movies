from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


# Create your views here.

def index(request):
    upcoming_movies = Movie.objects.all()
    context = {
        'upcoming_movies': upcoming_movies
    }
    return render(request, 'movies/index.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'movies/details.html', context)

def create(request):
    form = MovieForm(None)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully saved the movie details!!.")
            return redirect('/')
    return render(request, 'movies/create.html', { 'form': form })


def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(instance=movie)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated the movie details!!.")
            return redirect('movies:details', movie_id=movie_id)
    return render(request, 'movies/edit.html', { 'form': form })


def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    messages.success(request, "Successfully deleted the movie details!!.")    
    return redirect('/')