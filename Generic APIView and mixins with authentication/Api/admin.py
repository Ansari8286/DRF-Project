from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import PersonDetails
# Register your models here.
@admin.register(PersonDetails)
class pdAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'city', 'state', 'pincode','phone_number']