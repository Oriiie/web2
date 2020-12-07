from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
