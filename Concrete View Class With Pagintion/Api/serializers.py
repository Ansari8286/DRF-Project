from .models import HotelDetail
from rest_framework import serializers


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelDetail
        fields = '__all__'
