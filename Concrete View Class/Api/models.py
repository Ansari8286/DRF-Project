from django.db import models

# Create your models here.
class PersonDetails(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.name