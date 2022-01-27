from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='home'),
    # path('page/<int:pageNo>', Pagination, name='home'),
    path('single-page/<int:hid>', Hotel_Single_Page, name='single_page'),
]