from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'complete']


class MondayForm(forms.ModelForm):

    class Meta:
        model = Monday
        fields = ['title']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')