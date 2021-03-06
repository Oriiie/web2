# Generated by Django 3.1.3 on 2020-12-05 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
        migrations.RemoveField(
            model_name='note',
            name='notelist',
        ),
        migrations.RemoveField(
            model_name='scheduleday',
            name='schedulelist',
        ),
        migrations.DeleteModel(
            name='Homework',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='ScheduleDay',
        ),
    ]
