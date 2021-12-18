from django.db import models

# Create your models here.
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    position = models.ForeignKey('Position', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.pk}-{self.name}:{self.position}"


class Position(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.pk}-{self.title}"