# Generated by Django 4.0.3 on 2022-03-22 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_alter_student_options_progress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='progress',
            options={'verbose_name': 'Успеваемость', 'verbose_name_plural': 'Работы'},
        ),
        migrations.AddField(
            model_name='work',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='work',
            name='difficulty',
            field=models.CharField(choices=[('LOW', 'Низкая'), ('MIDDLE', 'Средняя'), ('HIGH', 'Высокая'), ('SPECIAL', 'Очень высокая')], default='MIDDLE', max_length=10),
        ),
    ]
