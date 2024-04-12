from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('movies:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)