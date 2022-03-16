from django.contrib import admin
from django.urls import path, include

#i nclude позволяет подгружать в url из проектов

urlpatterns = [
    path('study/', include('study.urls', namespace="study")),
    path('admin/', admin.site.urls),
]
