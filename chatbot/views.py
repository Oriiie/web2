from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
# Create your views here.


def start(request):
    return render(request, 'tasks/stayon.html')


@login_required(login_url="/sign-in")
def index(request):
    tasks = Task.objects.all().order_by('id')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('start')

    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/basic.html', context)


@login_required(login_url="/sign-in")
def bot(request):
    tasks = Task.objects.all().order_by('id')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            for i in tasks:
                if i.title == "Удалить":
                    tasks.delete()
                    break
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
        return redirect('start')


@login_required(login_url="/sign-in")
def update_task(request, pk):
    task = Task.objects.get(id=pk)

    if not task.complete:
        task.complete = True
        task.save()
        return redirect('start')

    if task.complete:
        task.complete = False
        task.save()
        return redirect('start')


@login_required(login_url="/sign-in")
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('start')


@login_required(login_url="/sign-in")
def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('start')
    return redirect('start')


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Имя пользователя или пароль не совпадают')
            return render(request, 'tasks/sign_in.html', {'form': form})
    else:
        form = AuthenticationForm()

    return render(request, 'tasks/sign_in.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('start')
    else:
        form = UserRegistrationForm()

    return render(request, 'tasks/sign_up.html', {'form': form})
