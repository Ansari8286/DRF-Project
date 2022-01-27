from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import HotelDetail
# Register your models here.
@admin.register(HotelDetail)
class pdAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotel_name', 'hotel_image', 'price', 'address']