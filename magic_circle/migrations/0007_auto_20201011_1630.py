# Generated by Django 3.1.2 on 2020-10-11 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magic_circle', '0006_magiccircle_date_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='MagicCircle',
        ),
    ]
