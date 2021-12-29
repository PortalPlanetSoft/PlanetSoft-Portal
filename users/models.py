from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
