from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    # Other driver-related fields

class Route(models.Model):
    name = models.CharField(max_length=100)
    # Other route-related fields

class Location(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
