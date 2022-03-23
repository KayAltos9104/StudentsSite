from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import *  # Чтобы работать с данными из моделей

# Я ниибу, почему он у меня в тегах html не робит без указания пространства имен


menu = [{'title': 'Успеваемость', 'url_name': 'study:groups'},
        {'title': 'Загрузить задание', 'url_name': 'study:create_obj'},
        {'title': 'Учебные материалы', 'url_name': 'study:index'},
        {'title': 'Контакты', 'url_name': 'study:about'},
        ]


def index(request):
    context = {'title': 'Учебный сайт',
               'menu': menu}
    return render(request, 'study/index.html', context=context)


def login(request):
    return HttpResponse('<h2>Заглушка страницы авторизации<h2>')


def groups(request):
    group_list = Group.objects.all().order_by('number')
    return render(request, 'study/groups.html', {'title': 'Список групп', 'groups': group_list})


def study_progress(request, group):
    students = Student.objects.all()
    works = Work.objects.all()
    progress = Progress.objects.all()
    list_w = []
    for s in students:
        if s.group_id==group:
            table = []
            for p in progress:
                if s.pk == p.student_id:
                    for w in works:
                        if w.pk == p.work_id:
                            # table.append({'surname': s.surname, 'w_name': w.name, 'status': p.status})
                            table.append({'w_name': w.name, 'status': p.status})
            list_w.append({'surname': s.surname, 'table': table})

    return render(request, 'study/progress.html', {'title': 'Успеваемость', 'headers': works, 'progress': list_w})


def add_objective(request):
    context = {'title': 'Учебный сайт',
               'menu': menu}
    name =""
    if request.method == "POST":
        name = request.POST.get("name")
        objective = Work.objects.create(name=name)
        objective.save()
        students = Student.objects.all()
        for s in students:
            progress = Progress.objects.create(student_id=s.pk, work_id=objective.pk)
            progress.save()
    return render(request, 'study/index.html', context=context)
    #return HttpResponse(f'<h2>Запись {name} создана<h2>')


def create_obj(request):
    return render(request, 'study/create_objective.html')


def about(request):
    return render(request, 'study/about.html')  # Адрес папки с проектом, если мы поместили ее именно в templates


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
