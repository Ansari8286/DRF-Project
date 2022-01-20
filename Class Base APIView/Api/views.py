from .models import PersonDetails
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonDetails
from .serializers import PersonSerializers
from django.core.exceptions import ValidationError
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
# Create your views here.

class CutomPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = "mypage"
    page_size_query_param = "records"
    max_page_size = 8
    last_page_string = "end"

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = "mylimit"
    offset_query_param = "myoffset"
    max_limit = 8

class CustomCursorPagination(CursorPagination):
    page_size = 5
    ordering = "name"
    cursor_query_param = "Name"

# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
class PersonAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    pagination_class = CutomPageNumberPagination
    serializer_class = PersonSerializers
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator
    def paginate_queryset(self, queryset):
        
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
    
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
        page = self.paginate_queryset(pd)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(pd, many=True)
        # serializer = PersonSerializers(pd, many=True)
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
