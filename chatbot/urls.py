from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name="index"),
    path('start', views.index, name="start"),
    path('bot', views.bot, name="bot"),
    path('botday', views.botday, name="botday"),
    path('schedule', views.schedule, name="schedule"),
    path('homework', views.homework, name="homework"),
    path('sign-up', views.sign_up, name="sign-up"),
    path('sign-in', views.sign_in, name="sign-in"),
    path('log-out', views.log_out, name="log-out"),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    path('schedule_delete_task/<str:pk>/', views.schedule_delete_task, name="schedule_delete_task"),
]
