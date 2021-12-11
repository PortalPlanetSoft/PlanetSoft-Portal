from django.db import models


class CompanyPosition(models.Model):
    department_name = models.CharField(max_length=100)
    position_name = models.CharField(max_length=100)
    office_number = models.IntegerField()


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # working position in the company
    position = models.ForeignKey(CompanyPosition, on_delete=models.CASCADE)
    # time joined the company
    time_joined = models.DateField(auto_now_add=True)
