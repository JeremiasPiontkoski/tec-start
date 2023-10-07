from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.street

class Location(models.Model):
    city = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    cep = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.city
   