from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader


def index(request):
    #return render(request, 'study/index.html')
    return HttpResponse('<h2>Заглушка основной страницы<h2>')


def login(request):
    return HttpResponse('<h2>Заглушка страницы авторизации<h2>')


def study_progress(request, group):
    return HttpResponse(f'<h2>Заглушка страницы успеваемости группы {group}<h2>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')




