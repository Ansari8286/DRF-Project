from .models import PersonDetails
from .serializers import PersonSerializers
from .serializers import PersonSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroy, RetrieveUpdateDestroyAPIView

# Create your views here.

class PersonListCreateView(ListCreateAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers


class PersonRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers
