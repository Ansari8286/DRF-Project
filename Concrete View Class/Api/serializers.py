from .models import PersonDetails
from rest_framework import serializers


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonDetails
        fields = '__all__'
