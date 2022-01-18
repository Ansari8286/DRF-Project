from email import message
from .models import PersonDetails
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PersonDetails
from .serializers import PersonSerializers
from .serializers import UserSerializer
from django.contrib.auth.models import User
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def personView(request, pk=None):
    if request.method == 'GET':
        id = pk
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

    if request.method == 'POST':
        serializer = PersonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        pd = PersonDetails.objects.get(id=id)
        serializer = PersonSerializers(pd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        pd = PersonDetails.objects.get(id=id)
        serializer = PersonSerializers(pd, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        pd = PersonDetails.objects.get(id=id)
        pd.delete()
        return Response({'msg':'Data DELETED'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
