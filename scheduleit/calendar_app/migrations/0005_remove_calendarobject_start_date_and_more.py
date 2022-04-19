# Generated by Django 4.0.3 on 2022-04-03 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0004_remove_calendarobject_start_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarobject',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='calendarobjectexception',
            name='start_date',
        ),
        migrations.AddField(
            model_name='calendarobject',
            name='start_time',
            field=models.TimeField(default='21:00:56'),
        ),
        migrations.AddField(
            model_name='calendarobjectexception',
            name='start_time',
            field=models.TimeField(default='21:00:56'),
        ),
    ]