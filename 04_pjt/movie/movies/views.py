from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, "movies/index.html", context)

@login_required
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect("movies:detail", movie.pk)
    else:
        form = MovieForm()
    context = {
        "form": form,
    }
    return render(request, "movies/create.html", context)


def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        "movie": movie,
    }
    return render(request, "movies/detail.html", context)

@login_required
def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect("movies:detail", movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        "form": form,
        "movie": movie,
    }
    return render(request, "movies/update.html", context)

@login_required
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        movie.delete()
    return redirect("movies:index")
