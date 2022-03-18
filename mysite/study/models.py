from django.db import models

class Groups (models.Model):
    number = models.CharField(max_length=5)
    study_year=models.IntegerField()


class Works(models.Model):
    name = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='photos/%m/%d')