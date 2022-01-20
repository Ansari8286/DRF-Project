from .models import PersonDetails
from .serializers import PersonSerializers
from .serializers import PersonSerializers
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
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
# Create your views here.

class PersonListCreateView(ListCreateAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers
    pagination_class = CutomPageNumberPagination

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class PersonRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
