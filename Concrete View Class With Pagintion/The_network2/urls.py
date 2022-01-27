from django.contrib import admin
from django.urls import path, include
from Api import views
from django.conf.urls.static import static
from django.conf import settings
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('personView/', views.PersonListCreateView.as_view()),
    path('personView/<int:pk>', views.PersonRetrieveUpdateDeleteView.as_view()),
    # path('personView/<int:pk>', views.PersonRetrieveView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)