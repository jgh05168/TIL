from django.db import models

# Create your models here.


class Weather(models.Model):
    temp = models.FloatField()
    feels_like = models.FloatField()
    dt_txt = models.DateTimeField() 