from django.db import models
from django.urls import reverse
import datetime


class Student (models.Model):
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name='Группа')

    def __str__(self):
        return self.surname + ' ' + self.name+'; Группа: '+str(self.group)

    class Meta: # Для отображения в админ-панели
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['group', 'surname']


class Group (models.Model):
    number = models.CharField(max_length=5, verbose_name='Номер группы')
    study_year = models.IntegerField(verbose_name='Год обучения')

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('study_progress', kwargs={'group_id': self.pk})

    class Meta:  # Для отображения в админ-панели
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Progress(models.Model):
    student = models.ForeignKey('Student', on_delete=models.PROTECT, verbose_name='Студент')
    work = models.ForeignKey('Work', on_delete=models.PROTECT, verbose_name='Задание')
    NO = 'Нет'
    REVIEW = 'Проверка'
    CORRECTION = 'Правки'
    COMPLETED = 'Сдано'
    STATUS = [(NO, 'Нет'), (REVIEW, 'Проверка'), (CORRECTION, 'Правки'), (COMPLETED, 'Сдано')]
    status = models.CharField(max_length=10, choices=STATUS, default=NO, verbose_name='Статус работы')
    comment = models.TextField(max_length=100, blank=True, null=True, verbose_name='Комментарий')

    class Meta:  # Для отображения в админ-панели
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        ordering = ['work']

    def __str__(self):
        return str(self.student)+'; '+str(self.work)+'; '+str(self.status)


class Work(models.Model):
    name = models.CharField(max_length=20, verbose_name='Задача')
    difficulty = models.CharField(max_length=15, verbose_name='Сложность')
    photo = models.ImageField(upload_to='photos/%m/%d', null=True, blank=True, verbose_name='Фото')
    LOW = 'LOW'
    MIDDLE = 'MIDDLE'
    HIGH = 'HIGH'
    SPECIAL = 'SPECIAL'
    DIFFICULTY = [(LOW, 'Низкая'), (MIDDLE, 'Средняя'), (HIGH, 'Высокая'), (SPECIAL, 'Очень высокая')]
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY, default=MIDDLE, verbose_name='Сложность')

    date = models.DateField(default=datetime.date.today, verbose_name='Дата задания', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:  # Для отображения в админ-панели
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['date']