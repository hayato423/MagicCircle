from django.db import models
from django.utils import timezone
# Create your models here.

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')


class MagicCircle(models.Model):
    corner = models.IntegerField(default=0)
    line = models.IntegerField(default=0)
    circle = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    date_time = models.DateTimeField(default=timezone.now())
