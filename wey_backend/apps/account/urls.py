from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api import *


urlpatterns = [
    path('me/', informationAboutUser, name='me'),
    path('signup/', signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('friend/request/<uuid:pk>/', sendFriendshipRequest),
]