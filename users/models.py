from django.contrib.auth.models import AbstractUser
from django.db import models


class CompanyPosition(models.Model):
    position_name = models.CharField(default="Undefined", max_length=100)

    def __str__(self):
        return self.position_name


class User(AbstractUser):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    WORK_LOCATION = [
        ('BL', 'Banja Luka'),
        ('BG', 'Beograd')
    ]
    is_admin = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField('first name', max_length=150)
    last_name = models.CharField('last name', max_length=150)
    email = models.EmailField('email address', unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
    work_location = models.CharField(max_length=2, choices=WORK_LOCATION, default='BL')
    company_position = models.ForeignKey(CompanyPosition, on_delete=models.PROTECT, default=None)
