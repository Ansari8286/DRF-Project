from django.contrib import admin
from django.urls import path, include
from Api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personView/', views.personListCreateView.as_view()),
    path('personView/<int:pk>/', views.personListRetrieveUpdateDestroyView.as_view()),
    path('register/', views.personRegisterCreateView.as_view()),
    path('gettoken/', TokenObtainPairView.as_view(), name ='get_token'),
    path('verifiy/', TokenVerifyView.as_view(), name ='token_verify'),
    path('refresh/', TokenRefreshView.as_view(), name ='token_refresh'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
