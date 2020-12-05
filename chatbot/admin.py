from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(List)
admin.site.register(Homework)
admin.site.register(Note)
admin.site.register(ScheduleDay)
