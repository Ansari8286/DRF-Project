from rest_framework import serializers
from .models import PersonDetails

# Validator
def Start_With_Four(value):
    if value[0] != '4':
        raise serializers.ValidationError("Pin code must start with 4")

class PersonDetailsSerializer(serializers.ModelSerializer):
    pincode = serializers.CharField(max_length=200, validators=[Start_With_Four])

    class Meta:
        model = PersonDetails
        fields = ['name', 'address', 'city', 'state', 'country', 'pincode', 'phone_number', 'email']

    
    # Field lavel validation
    def validate_phone_number(self, value):
        if (len(value)) >= 11:
            raise serializers.ValidationError("You enter wrong number")
        return value

    # Object level validation
    def validate(self, data):
        state_name = data.get('state')
        country_name = data.get('country')
        if state_name ==  country_name:
            raise serializers.ValidationError("You enter same state and country name")
        return data

# class PersonDetailsSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     address = serializers.CharField(max_length=200)
#     city = serializers.CharField(max_length=200)
#     state = serializers.CharField(max_length=200)
#     country = serializers.CharField(max_length=200)
#     pincode = serializers.CharField(max_length=200, validators=[Start_With_Four])
#     phone_number = serializers.CharField(max_length=200)
#     email = serializers.CharField(max_length=200)


    # def create(self, validated_data):
    #     return PersonDetails.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.state = validated_data.get('state', instance.state)
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.pincode = validated_data.get('pincode', instance.pincode)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance
