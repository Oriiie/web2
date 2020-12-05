from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

from .models import *


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'notneeded']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'done']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class ScheduleDayForm(forms.ModelForm):
    class Meta:
        model = ScheduleDay
        fields = ['title', 'time']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательно к вводу, введите действующую электронную почту',
                             required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'passwordconfirm')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()

        if not any(i in email for i in ('.ru', '.com', '.ua', '.net')):
            raise forms.ValidationError('Введите корректный адрес')

        if user_count > 0:
            raise forms.ValidationError('Такая электронная почта уже есть в базе данных')
        return email


class UserEmailEditForm(UserChangeForm):
    email = forms.EmailField(max_length=254, help_text='Обязательно к вводу, введите действующую электронную почту',
                             required=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()

        if not any(i in email for i in ('.ru', '.com', '.ua', '.net')):
            raise forms.ValidationError('Введите корректный адрес')

        if user_count > 0:
            raise forms.ValidationError('Такая электронная почта уже есть в базе данных')
        return email
