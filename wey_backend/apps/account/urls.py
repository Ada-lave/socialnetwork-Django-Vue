from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api import *


urlpatterns = [
    path('me/', informationAboutUser, name='me'),
    path('signup/', signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('friends/<uuid:pk>/request/', sendFriendshipRequest),
    path('profile/friends/<uuid:pk>/', friendsRequest),
    path('profile/friends/<uuid:id>/<str:status>/', handleRequest)
]