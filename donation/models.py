from django.db import models
from city.models import City
from django.utils import timezone

class Donation(models.Model):
    description = models.TextField()
    cpf = models.CharField(max_length=20)
    person_name = models.CharField(max_length=100)
    key_pix = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='donations')
    date_send = models.DateTimeField(default=timezone.now)