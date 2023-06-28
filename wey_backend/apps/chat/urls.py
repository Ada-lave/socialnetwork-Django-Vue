from django.urls import path
from .api import *
urlpatterns = [
    path('',conversitionList, name='convList'),
    path('<uuid:pk>/', conversitionDetail, name='conversitionDetail'),
    path('<uuid:pk>/send/', conversitionSendMessage, name='conversitionSendMessage'),
]