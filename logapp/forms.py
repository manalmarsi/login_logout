# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Formulaire d'inscription
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Formulaire de connexion
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
