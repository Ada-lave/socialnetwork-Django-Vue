from django.urls import path
from .api import *
urlpatterns = [
    path('',conversitionList, name='convList')
]