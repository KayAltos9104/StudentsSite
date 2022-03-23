# Generated by Django 4.0.3 on 2022-03-23 07:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0008_alter_progress_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
        migrations.AlterField(
            model_name='group',
            name='number',
            field=models.CharField(max_length=5, verbose_name='Номер группы'),
        ),
        migrations.AlterField(
            model_name='group',
            name='study_year',
            field=models.IntegerField(verbose_name='Год обучения'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='comment',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='status',
            field=models.CharField(choices=[('Нет', 'Нет'), ('Проверка', 'Проверка'), ('Правки', 'Правки'), ('Сдано', 'Сдано')], default='Нет', max_length=10, verbose_name='Статус работы'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='study.group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата задания'),
        ),
        migrations.AlterField(
            model_name='work',
            name='difficulty',
            field=models.CharField(choices=[('LOW', 'Низкая'), ('MIDDLE', 'Средняя'), ('HIGH', 'Высокая'), ('SPECIAL', 'Очень высокая')], default='MIDDLE', max_length=10, verbose_name='Сложность'),
        ),
        migrations.AlterField(
            model_name='work',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Работа'),
        ),
        migrations.AlterField(
            model_name='work',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%m/%d', verbose_name='Фото'),
        ),
    ]
