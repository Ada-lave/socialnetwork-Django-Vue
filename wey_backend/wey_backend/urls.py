from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.account.views import *    

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('apps.account.urls')),
    path('api/posts/', include('apps.post.urls')),
    path('api/search/', include('apps.search.urls')),
    path('api/chat/',include('apps.chat.urls')),
    path('api/notification/',include('apps.notification.urls')),

    path('activate/',activateEmail,name='activateEmail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
