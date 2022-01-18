from django.contrib import admin
from django.urls import path
from Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personView/', views.PersonListCreateView.as_view()),
    path('personView/<int:pk>', views.PersonRetrieveUpdateDeleteView.as_view()),
]