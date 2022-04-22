from datetime import datetime

from django.contrib.auth import user_logged_in
from django.contrib.auth.models import AbstractUser, update_last_login
from django.db import models

from events.models import Event
from users.constants import GENDER_CHOICES, WORK_LOCATION


class CompanyPosition(models.Model):
    position_name = models.CharField(default="Undefined", max_length=100)

    def __str__(self):
        return self.position_name


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)
    first_name = models.CharField('first name', max_length=150)
    last_name = models.CharField('last name', max_length=150)
    email = models.EmailField('email address', unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    work_location = models.CharField(max_length=2, choices=WORK_LOCATION, default='BL')
    company_position = models.ForeignKey(CompanyPosition, on_delete=models.PROTECT, default=None)
    profile_pic = models.ImageField(upload_to='avatars/', null=True, blank=True)
    birth_date = models.DateField(null=True, default=None, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    business_phone = models.CharField(max_length=15, null=True, blank=True)
    previous_login = models.DateTimeField('previous login', blank=True, null=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        obj, created = Event.objects.update_or_create(
            title="Rođendan "+self.first_name + ' ' + self.last_name,
            type='Rođendan',
            details="Rođendan "+self.first_name + ' ' + self.last_name + '(' + self.username + ')',
            defaults={
                'start_time': self.birth_date,
                'author': self,
            }
        )
        obj.shared.set(User.objects.all())

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.username + ')'


def update_last_and_previous_login(sender, user, **kwargs):
    user.previous_login = user.last_login
    user.last_login = datetime.now()
    user.save(update_fields=["previous_login", "last_login"])


user_logged_in.disconnect(update_last_login, dispatch_uid="update_last_login")
user_logged_in.connect(update_last_and_previous_login, dispatch_uid="update_last_and_previous_login")
