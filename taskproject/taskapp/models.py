from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.


class department(models.Model):
    departmentname = models.CharField(max_length=100)


class employee(models.Model):
    deptid = models.ForeignKey(department, on_delete=CASCADE)
    empname = models.CharField(max_length=100)
