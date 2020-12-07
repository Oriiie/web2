from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name="index"),
    path('start', views.index, name="start"),
    path('bot', views.bot, name="bot"),
    path('botmonday', views.botmonday, name="botmonday"),
    path('bottuesday', views.bottuesday, name="bottuesday"),
    path('botwednesday', views.botwednesday, name="botwednesday"),
    path('botthursday', views.botthursday, name="botthursday"),
    path('schedule', views.schedule, name="schedule"),
    path('mondayschedule', views.mondayschedule, name='mondayschedule'),
    path('tuesdayschedule', views.tuesdayschedule, name='tuesdayschedule'),
    path('wednesdayschedule', views.wednesdayschedule, name='wednesdayschedule'),
    path('thursdayschedule', views.thursdayschedule, name='thursdayschedule'),
    path('homework', views.homework, name="homework"),
    path('sign-up', views.sign_up, name="sign-up"),
    path('sign-in', views.sign_in, name="sign-in"),
    path('log-out', views.log_out, name="log-out"),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    path('monday_delete_task/<str:pk>/', views.monday_delete_task, name="monday_delete_task"),
    path('tuesday_delete_task/<str:pk>/', views.tuesday_delete_task, name="tuesday_delete_task"),
    path('wednesday_delete_task/<str:pk>/', views.wednesday_delete_task, name="wednesday_delete_task"),
    path('thursday_delete_task/<str:pk>/', views.thursday_delete_task, name="thursday_delete_task"),
]
