from django.db import models

# Create your models here.
class Employee(models.Model):
    employeename = models.CharField(max_length=200)
    employeestartdate = models.CharField(max_length=200)
    employeeclass = models.CharField(max_length=500)
    employeegender = models.BooleanField(default=False)