from django.contrib import admin
from django.urls import path, include
from Api import views
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('personView', views.PersonAPIView, basename='person')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('personView/', views.PersonAPIView.as_view()),
    path('personView/<int:pk>', obtain_auth_token),

    # path('gettoken/', views.PersonAPIView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]