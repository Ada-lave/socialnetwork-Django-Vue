from django.urls import path
from .api import *

urlpatterns = [
    path('allUser/', notification, name='notifications'),
    path('read/<uuid:pk>/', readNotification, name='readnoti')
]