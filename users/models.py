from django.contrib.auth.models import AbstractUser
from django.db import models


class CompanyPosition(models.Model):
    position_name = models.CharField(default="Undefined", max_length=100)

    def __str__(self):
        return self.position_name


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    gender = models.BooleanField(default=False)
    company_position = models.ForeignKey(CompanyPosition, on_delete=models.PROTECT, default=None)
