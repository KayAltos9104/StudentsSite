# Generated by Django 4.0.3 on 2022-03-22 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_rename_groups_group_rename_works_work'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['group', 'surname'], 'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Нет', 'Нет'), ('Проверка', 'Проверка'), ('Правки', 'Правки'), ('Сдано', 'Сдано')], default='Нет', max_length=10)),
                ('comment', models.TextField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='study.student')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='study.work')),
            ],
        ),
    ]