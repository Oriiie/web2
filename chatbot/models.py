from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.


class List(models.Model):
    """Общий формат списка, контейнер любого вида записей"""
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Note(models.Model):
    """Заметка"""
    title = models.CharField(max_length=250)
    notneeded = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    notelist = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Homework(models.Model):
    """Домашняя работа на предмет"""
    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    homeworklist = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ScheduleDay(models.Model):
    """Расписание дня и/или расписание консультаций"""
    title = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    schedulelist = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title