from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Comment
from django.contrib.auth.decorators import login_required
from .forms import MovieForm, CommentForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    form = CommentForm()
    context= {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@login_required
def update(request, user_pk):
    movie = Movie.objects.get(pk=user_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)

@login_required
def delete(request, user_pk):
    movie = Movie.objects.get(pk=user_pk)
    movie.delete()
    return redirect('movies:index')

@login_required
def comments_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('movies:detail', movie.pk)

def comments_delete(request, movie_pk, comment_pk):
    pass