# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required




@login_required
def home(request):
    return render(request, 'home.html')

# Inscription
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirige vers une page d'accueil ou autre
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

# Connexion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirige vers une page d'accueil ou autre
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Déconnexion
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige vers la page d'accueil
