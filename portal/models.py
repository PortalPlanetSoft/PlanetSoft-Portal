from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, null='false')
    body = models.TextField(null='false')
    slug = models.SlugField(null='false', unique='true')


class CompanyPosition(models.Model):
    department_name = models.CharField(max_length=100, null='false')
    position_name = models.CharField(max_length=100, null='false')
    office_number = models.IntegerField()


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null='false')
    last_name = models.CharField(max_length=125, null='false')
    position = models.ForeignKey(CompanyPosition, on_delete=models.CASCADE)
    time_joined = models.DateField()