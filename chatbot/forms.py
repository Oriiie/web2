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


class TuesdayForm(forms.ModelForm):

    class Meta:
        model = Tuesday
        fields = ['title']


class WednesdayForm(forms.ModelForm):

    class Meta:
        model = Wednesday
        fields = ['title']


class ThursdayForm(forms.ModelForm):

    class Meta:
        model = Thursday
        fields = ['title']


class FridayForm(forms.ModelForm):

    class Meta:
        model = Friday
        fields = ['title']


class ConsultForm(forms.ModelForm):

    class Meta:
        model = Consult
        fields = ['title']


class HomeworkImportantForm(forms.ModelForm):

    class Meta:
        model = HomeworkImportant
        fields = ['title']


class HomeworkMediumForm(forms.ModelForm):

    class Meta:
        model = HomeworkMedium
        fields = ['title']


class HomeworkEasyForm(forms.ModelForm):

    class Meta:
        model = HomeworkEasy
        fields = ['title']

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')