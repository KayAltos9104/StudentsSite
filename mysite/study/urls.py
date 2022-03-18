from django.urls import path

from . import views

app_name = 'study'

urlpatterns = [
    path('', views.index, name='index'),  # http://127.0.0.1:8000/study/
    path('login/', views.login, name='login'),  # http://127.0.0.1:8000/study/login/
    path('study_progress/<str:group>/', views.study_progress, name='study_progress'),
    # http://127.0.0.1:8000/study/study_progress/num/
    # адрес страницы, ссылка на функцию, имя внутри программы (например, для использования в шаблонах)
    path('about/', views.about, name='about'),
    path('groups/', views.groups, name='groups'),
]