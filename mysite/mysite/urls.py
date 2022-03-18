from django.contrib import admin
from django.urls import path, include
from study.views import *
from mysite import settings
from django.conf.urls.static import static

#include позволяет подгружать в url из проектов

urlpatterns = [
    path('study/', include('study.urls', namespace="study")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found