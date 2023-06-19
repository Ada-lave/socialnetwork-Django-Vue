
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('apps.account.urls')),
    path('api/posts/', include('apps.post.urls')),
]
