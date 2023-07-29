from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    last_watered = models.DateTimeField()
    water_frequency = models.IntegerField()
