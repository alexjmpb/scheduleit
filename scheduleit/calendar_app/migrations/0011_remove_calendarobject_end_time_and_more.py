# Generated by Django 4.0.3 on 2022-04-22 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0010_calendarobject_tz_offset_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarobject',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='calendarobject',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='calendarobject',
            name='tz_offset',
        ),
        migrations.RemoveField(
            model_name='calendarobjectexception',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='calendarobjectexception',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='calendarobjectexception',
            name='tz_offset',
        ),
        migrations.AddField(
            model_name='calendarobject',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 18, 18, 35, 467382)),
        ),
        migrations.AddField(
            model_name='calendarobjectexception',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 18, 18, 35, 467382)),
        ),
        migrations.AlterField(
            model_name='calendarobject',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 18, 18, 35, 467382)),
        ),
        migrations.AlterField(
            model_name='calendarobjectexception',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 18, 18, 35, 467382)),
        ),
    ]