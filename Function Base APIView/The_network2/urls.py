from django.contrib import admin
from django.urls import path, include
from Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personView/', views.personView),
    path('personView/<int:pk>', views.personView),
    path('register/', views.create_auth),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]