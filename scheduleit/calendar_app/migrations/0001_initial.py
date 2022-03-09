# Generated by Django 4.0.3 on 2022-03-09 01:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default='', max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_fully_day', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 21, 51, 12, 524497, tzinfo=utc))),
                ('is_recurring', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default='', max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_fully_day', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_recurring', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskRecurrencePattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_date', models.DateField(default=django.utils.timezone.now)),
                ('recurrence', models.PositiveIntegerField(default=0)),
                ('parent_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskException',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default='', max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_fully_day', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('occurrence_number', models.PositiveIntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('original_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventRecurrencePattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_date', models.DateField(default=django.utils.timezone.now)),
                ('recurrence', models.PositiveIntegerField(default=0)),
                ('parent_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventException',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default='', max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_fully_day', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime(2022, 3, 8, 21, 51, 12, 524497, tzinfo=utc))),
                ('occurrence_number', models.PositiveIntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('original_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]