# Generated by Django 4.0.3 on 2022-03-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0007_alter_progress_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='comment',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
