from .models import PersonDetails
from .serializers import PersonSerializers, UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
    
class personListCreateView(ListCreateAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class personListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class personRegisterCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
