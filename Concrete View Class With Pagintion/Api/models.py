from django.db import models

# Create your models here.
class HotelDetail(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.hotel_name
