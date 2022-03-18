from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import * # Чтобы работать с данными из моделей

def index(request):
    return render(request, 'study/index.html', {'title': 'Учебный сайт'})
    #return HttpResponse('<h2>Заглушка основной страницы<h2>')


def login(request):
    return HttpResponse('<h2>Заглушка страницы авторизации<h2>')



def groups(request):
    group_list = Groups.objects.all().order_by('number')
    return render(request, 'study/groups.html', {'title': 'Список групп', 'groups': group_list})


def study_progress(request, group):
    return HttpResponse(f'<h2>Заглушка страницы успеваемости группы {group}<h2>')
    #return render(request, 'study/groups.html', {'group': group})


def about(request):
    return render(request, 'study/about.html')  # Адрес папки с проектом, если мы поместили ее именно в templates


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')

