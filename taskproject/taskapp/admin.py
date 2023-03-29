from django.contrib import admin

from taskapp.models import department, employee

# Register your models here.

admin.site.register(department)
admin.site.register(employee)