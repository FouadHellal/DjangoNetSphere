from django.db import models

class Temperature(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()

class Humidity(models.Model):
    timestamp = models.DateTimeField()
    humidity = models.FloatField()
class Preassure(models.Model):
    timestamp = models.DateTimeField()
    preassure = models.FloatField()
