# Generated by Django 3.1.2 on 2020-10-09 13:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magic_circle', '0005_auto_20201009_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='magiccircle',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 9, 13, 23, 37, 562064, tzinfo=utc)),
        ),
    ]
