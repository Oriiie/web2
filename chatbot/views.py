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
def schedule(request):
    monday = Monday.objects.filter(user_id=request.user.id).order_by('id')
    tuesday = Tuesday.objects.filter(user_id=request.user.id).order_by('id')
    wednesday = Wednesday.objects.filter(user_id=request.user.id).order_by('id')
    thursday = Thursday.objects.filter(user_id=request.user.id).order_by('id')
    friday = Friday.objects.filter(user_id=request.user.id).order_by('id')
    consult = Consult.objects.filter(user_id=request.user.id).order_by('id')

    mondayform = MondayForm()
    tuesdayform = TuesdayForm()
    wednesdayform = WednesdayForm()
    thursdayform = ThursdayForm()
    fridayform = FridayForm()
    consultform = ConsultForm()
    context = {'monday': monday, 'tuesday': tuesday,
               'mondayform': mondayform, 'tuesdayform': tuesdayform,
               'wednesday': wednesday, 'wednesdayform': wednesdayform,
               'thursday': thursday, 'thursdayform': thursdayform,
               'friday': friday, 'fridayform': fridayform,
               'consult': consult, 'consultform': consultform}
    return render(request, 'tasks/schedule.html', context)


@login_required(login_url="/sign-in")
def mondayschedule(request):
    monday = Monday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        mondayform = MondayForm(request.POST)
        if mondayform.is_valid():
            instance = mondayform.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in monday:
                if len(monday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')
    mondayform = MondayForm()
    context = {'monday': monday, 'mondayform': mondayform}
    return render(request, 'tasks/schedule.html', context)


@login_required(login_url="/sign-in")
def tuesdayschedule(request):
    tuesday = Tuesday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        tuesdayform = TuesdayForm(request.POST)
        if tuesdayform.is_valid():
            instance = tuesdayform.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in tuesday:
                if len(tuesday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')
    tuesdayform = TuesdayForm()
    context = {'tuesday': tuesday, 'tuesdayform': tuesdayform}
    return render(request, 'tasks/schedule.html', context)


@login_required(login_url="/sign-in")
def wednesdayschedule(request):
    wednesday = Wednesday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        wednesdayform = WednesdayForm(request.POST)
        if wednesdayform.is_valid():
            instance = wednesdayform.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in wednesday:
                if len(wednesday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')
    wednesdayform = WednesdayForm()
    context = {'wednesday': wednesday, 'wednesdayform': wednesdayform}
    return render(request, 'tasks/schedule.html', context)


@login_required(login_url="/sign-in")
def thursdayschedule(request):
    thursday = Thursday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        thursdayform = ThursdayForm(request.POST)
        if thursdayform.is_valid():
            instance = thursdayform.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in thursday:
                if len(thursday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')
    thursdayform = ThursdayForm()
    context = {'thursday': thursday, 'thursdayform': thursdayform}
    return render(request, 'tasks/schedule.html', context)


@login_required(login_url="/sign-in")
def fridayschedule(request):
    friday = Friday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        fridayform = FridayForm(request.POST)
        if fridayform.is_valid():
            instance = fridayform.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in friday:
                if len(friday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')
    fridayform = FridayForm()
    context = {'friday': friday, 'fridayform': fridayform}
    return render(request, 'tasks/schedule.html', context)


@login_required(login_url="/sign-in")
def consultschedule(request):
    consult = Consult.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        consultform = ConsultForm(request.POST)
        if consultform.is_valid():
            instance = consultform.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('schedule')
    consultform = ConsultForm()
    context = {'consult': consult, 'consultform': consultform}
    return render(request, 'tasks/schedule.html', context)


@login_required(login_url="/sign-in")
def monday_delete_task(request, pk):
    task = Monday.objects.get(id=pk)
    task.delete()
    return redirect('schedule')


@login_required(login_url="/sign-in")
def tuesday_delete_task(request, pk):
    task = Tuesday.objects.get(id=pk)
    task.delete()
    return redirect('schedule')


@login_required(login_url="/sign-in")
def wednesday_delete_task(request, pk):
    task = Wednesday.objects.get(id=pk)
    task.delete()
    return redirect('schedule')


@login_required(login_url="/sign-in")
def thursday_delete_task(request, pk):
    task = Thursday.objects.get(id=pk)
    task.delete()
    return redirect('schedule')


@login_required(login_url="/sign-in")
def friday_delete_task(request, pk):
    task = Friday.objects.get(id=pk)
    task.delete()
    return redirect('schedule')


@login_required(login_url="/sign-in")
def consult_delete_task(request, pk):
    task = Consult.objects.get(id=pk)
    task.delete()
    return redirect('schedule')


@login_required(login_url="/sign-in")
def hardhomework_delete_task(request, pk):
    task = HomeworkImportant.objects.get(id=pk)
    task.delete()
    return redirect('homework')


@login_required(login_url="/sign-in")
def mediumhomework_delete_task(request, pk):
    task = HomeworkMedium.objects.get(id=pk)
    task.delete()
    return redirect('homework')


@login_required(login_url="/sign-in")
def homework(request):
    hardhomework = HomeworkImportant.objects.filter(user_id=request.user.id).order_by('id')
    mediumhomework = HomeworkMedium.objects.filter(user_id=request.user.id).order_by('id')

    hardhomeworkform = HomeworkImportantForm()
    mediumhomeworkform = HomeworkMediumForm()
    context = {'hardhomework': hardhomework, 'hardhomeworkform': hardhomeworkform,
               'mediumhomework': mediumhomework, 'mediumhomeworkform': mediumhomeworkform}
    return render(request, 'tasks/homework.html', context)


@login_required(login_url="/sign-in")
def hardhomework(request):
    hardhomework = HomeworkImportant.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        hardhomeworkform = HomeworkImportantForm(request.POST)
        if hardhomeworkform.is_valid():
            instance = hardhomeworkform.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('homework')
    hardhomeworkform = HomeworkImportantForm()
    context = {'hardhomework': hardhomework, 'hardhomeworkform': hardhomeworkform}
    return render(request, 'tasks/homework.html', context)


@login_required(login_url="/sign-in")
def mediumhomework(request):
    mediumhomework = HomeworkMedium.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        mediumhomeworkform = HomeworkMediumForm(request.POST)
        if mediumhomeworkform.is_valid():
            instance = mediumhomeworkform.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('homework')
    mediumhomeworkform = HomeworkMediumForm()
    context = {'mediumhomework': mediumhomework, 'mediumhomeworkform': mediumhomeworkform}
    return render(request, 'tasks/homework.html', context)


@login_required(login_url="/sign-in")
def index(request):
    tasks = Note.objects.filter(user_id=request.user.id).order_by('id')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('start')

    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/basic.html', context)


@login_required(login_url="/sign-in")
def bot(request):
    tasks = Note.objects.filter(user_id=request.user.id).order_by('id')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in tasks:
                if i.title == "Удалить":
                    tasks.delete()
                    break
            for i in tasks:
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
        return redirect('start')


@login_required(login_url="/sign-in")
def botmonday(request):
    monday = Monday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        form = MondayForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in monday:
                if i.title == "Удалить":
                    monday.delete()
                    break
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
            for i in monday:
                if len(monday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')


@login_required(login_url="/sign-in")
def bottuesday(request):
    tuesday = Tuesday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        form = TuesdayForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in tuesday:
                if i.title == "Удалить":
                    tuesday.delete()
                    break
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
            for i in tuesday:
                if len(tuesday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')


@login_required(login_url="/sign-in")
def botwednesday(request):
    wednesday = Wednesday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        form = WednesdayForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in wednesday:
                if i.title == "Удалить":
                    wednesday.delete()
                    break
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
            for i in wednesday:
                if len(wednesday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')


@login_required(login_url="/sign-in")
def botthursday(request):
    thursday = Thursday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        form = ThursdayForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in thursday:
                if i.title == "Удалить":
                    thursday.delete()
                    break
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
            for i in thursday:
                if len(thursday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')


@login_required(login_url="/sign-in")
def botfriday(request):
    friday = Friday.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        form = FridayForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in friday:
                if i.title == "Удалить":
                    friday.delete()
                    break
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
            for i in friday:
                if len(friday) > 4:
                    i.delete()
                    return redirect('schedule')
        return redirect('schedule')


@login_required(login_url="/sign-in")
def bothardhomework(request):
    hardhomework = HomeworkImportant.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        form = HomeworkImportantForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in hardhomework:
                if i.title == "Удалить":
                    hardhomework.delete()
                    break
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
        return redirect('homework')


@login_required(login_url="/sign-in")
def botmediumhomework(request):
    mediumhomework = HomeworkMedium.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        form = HomeworkMediumForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in mediumhomework:
                if i.title == "Удалить":
                    mediumhomework.delete()
                    break
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
        return redirect('homework')


@login_required(login_url="/sign-in")
def botconsult(request):
    consult = Consult.objects.filter(user_id=request.user.id).order_by('id')
    if request.method == 'POST':
        form = ConsultForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            for i in consult:
                if i.title == "Удалить":
                    consult.delete()
                    break
                if i.title == "Помощь":
                    i.delete()
                    return render(request, 'tasks/help.html')
        return redirect('schedule')


@login_required(login_url="/sign-in")
def update_task(request, pk):
    task = Note.objects.get(id=pk)

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
    task = Note.objects.get(id=pk)
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
