from django.contrib import admin
from .models import *


class ProgressAdmin (admin.ModelAdmin):
    search_fields = ('student', 'work')


admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Work)
admin.site.register(Progress, ProgressAdmin)
