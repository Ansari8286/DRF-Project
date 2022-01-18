from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import PersonDetails
from .serializers import PersonDetailsSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
# Create your views here.

def person(request, all):
    if request.method == 'GET':
        pd = PersonDetails.objects.get(id=all)
        pds = PersonDetailsSerializer(pd)
        return JsonResponse(pds.data, safe=False)


@csrf_exempt
def personView(request):
    if request.method == 'GET':
        pd = PersonDetails.objects.all()
        pds = PersonDetailsSerializer(pd, many=True)
        return JsonResponse(pds.data, safe=False)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = PersonDetailsSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Data created'}
            # json_data = JSONRenderer().render(msg)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(msg, safe=False)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        pd = PersonDetails.objects.get(id=id)
        serializer = PersonDetailsSerializer(pd, data=py_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Data Updated'}
            return JsonResponse(msg, safe=False)
        return JsonResponse(serializer.errors, safe=False)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        pd = PersonDetails.objects.get(id=id)
        pd.delete()
        msg = {'msg': 'Data Deleted!!'}
        return JsonResponse(msg, safe=False)
