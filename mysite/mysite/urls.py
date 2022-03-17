from django.contrib import admin
from django.urls import path, include
from study.views import *

#include позволяет подгружать в url из проектов

urlpatterns = [
    path('study/', include('study.urls', namespace="study")),
    path('admin/', admin.site.urls),
]

handler404 = page_not_found