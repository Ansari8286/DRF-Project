from .models import PersonDetails
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonDetails
from .serializers import PersonSerializers
from django.core.exceptions import ValidationError
# Create your views here.

class PersonAPIView(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            try:
                pd = PersonDetails.objects.get(id=id)
                serializer = PersonSerializers(pd)
                return Response(serializer.data)
            except:
                message = {'message': 'No date avilable'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        pd = PersonDetails.objects.all()
        serializer = PersonSerializers(pd, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PersonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, obj_id):
        try:
            return PersonDetails.objects.get(id=obj_id)
        except (PersonDetails.DoesNotExist, ValidationError):
            raise status.HTTP_400_BAD_REQUEST

    def validate_ids(self, id_list):
        for id in id_list:
            try:
                PersonDetails.objects.get(id=id)
            except (PersonDetails.DoesNotExist, ValidationError):
                raise status.HTTP_400_BAD_REQUEST
        return True

    def put(self, request, pk=None, format=None):
        data = request.data
        print(data, 'request data')
        person_ids = [i['id'] for i in data]
        self.validate_ids(person_ids)
        instances = []
        for temp_dict in data:
            person_id = temp_dict['id']
            print(person_id, 'person id')
            name = temp_dict['name']
            address = temp_dict['address']
            city = temp_dict['city']
            state = temp_dict['state']
            pincode = temp_dict['pincode']
            phone_number = temp_dict['phone_number']
            obj = self.get_object(person_id)
            print(obj, 'objects')
            obj.name = name
            obj.description = address
            obj.city = city
            obj.state = state
            obj.pincode = pincode
            obj.phone_number = phone_number
            obj.save()
            instances.append(obj)
        serializer = PersonSerializers(instances, many=True)
        return Response(serializer.data)

        # id = pk
        # pd = PersonDetails.objects.get(id=id)
        # serializer = PersonSerializers(pd, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        id = pk
        pd = PersonDetails.objects.get(id=id)
        serializer = PersonSerializers(pd, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        id = pk
        pd = PersonDetails.objects.get(id=id)
        pd.delete()
        return Response(pd.data, status=status.HTTP_200_OK)
