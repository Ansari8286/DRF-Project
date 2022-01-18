from django.contrib import admin
from django.urls import path
from Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personView/', views.PersonAPIView.as_view()),
    path('personView/<int:pk>', views.PersonAPIView.as_view()),
]