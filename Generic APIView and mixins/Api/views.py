from .models import PersonDetails
from .models import PersonDetails
from .serializers import PersonSerializers
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
# Create your views here.

class PersonListCreateView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PersonRetrieveUpdateDeleteView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
