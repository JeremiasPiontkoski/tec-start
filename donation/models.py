from django.db import models
from city.models import City
from django.utils import timezone

class Donation(models.Model):
    PATH_IMAGES = 'donations/images/%Y/%m/%d'
    description = models.TextField()
    cpf = models.CharField(max_length=20)
    person_name = models.CharField(max_length=100)
    key_pix = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='donations')
    date_send = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=PATH_IMAGES, verbose_name='Imagem')

    def __str__(self) -> str:
        return self.description