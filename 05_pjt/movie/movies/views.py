from django.shortcuts import render, redirect
from .forms import MovieForm, CommentForm
from .models import Movie, Comment


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm()
    context = {
        'movie': movie,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
    }
    return render(request, 'movies/update.html', context)

def delete(request, movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        movie.delete()
    return redirect('movies:index')

def comments_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit = False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', movie.pk)

    context = {
        'comment_form':comment_form,
        'movie':movie,
        'comments':comments,
    }
    return render(request,'movies/detail.html', context)

def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)