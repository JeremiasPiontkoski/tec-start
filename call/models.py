from django.db import models
from city.models import City

class Call(models.Model):
    phone = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='calls')
    cpf = models.CharField(max_length=20)
    person_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.person_name