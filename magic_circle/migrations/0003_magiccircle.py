# Generated by Django 3.1.2 on 2020-10-09 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic_circle', '0002_remove_image_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagicCircle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corner', models.IntegerField()),
                ('line', models.IntegerField()),
                ('circle', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]