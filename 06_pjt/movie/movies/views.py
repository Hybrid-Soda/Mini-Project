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
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comment_set.all()
    form = CommentForm()
    context= {
        'movie': movie,
        'form': form,
        'comments': comments
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
def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
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
def delete(request, movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
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

@login_required
def comments_delete(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('movies:detail', movie_pk)

@login_required
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:index')

@login_required
def create_reply(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        reply_comment = form.save(commit=False)
        reply_comment.user = request.user
        reply_comment.movie = comment.movie
        reply_comment.parent_comment = comment
        reply_comment.save()
        return redirect('movies:detail', comment.movie.pk)