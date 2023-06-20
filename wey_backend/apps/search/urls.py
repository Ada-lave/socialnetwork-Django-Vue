from django.urls import path
from .api import search

urlpatterns = [
    path('', search, name='search')
]