from django.db import models

class Employee(models.Model):
    employeeName = models.CharField(max_length=200)
    employeeDateOfJoining = models.CharField(max_length=200)
    employeeDepartment = models.CharField(max_length=500)
    employeeGender = models.BooleanField(default=False)
# Create your models here.
