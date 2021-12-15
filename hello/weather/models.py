from django.db import models


class City(models.Model):
    title = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    lat = models.FloatField(unique=True)
    lon = models.FloatField(unique=True)


class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    date = models.DateField()
    data_weather = models.JSONField()
    hourly_weather = models.JSONField()
