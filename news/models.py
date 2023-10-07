from django.db import models
from city.models import City

class New(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=1000)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='news')
