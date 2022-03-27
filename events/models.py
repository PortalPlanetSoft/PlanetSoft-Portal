from django.db import models

from users.models import User


class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    shared = models.ManyToManyField('Organizator', to=User, related_name='shared')
    title = models.CharField('Naslov', max_length=48)
    details = models.CharField('Opis', max_length=256, null=True, blank=True)
    start_time = models.DateTimeField('Početak događaja')
    end_time = models.DateTimeField('Kraj događaja', null=True, blank=True)
    repeat_days = models.IntegerField('Ponavi po danima', default=0, null=True, blank=True)
    repeat_every_year = models.BooleanField('Ponovi svake godine', default=False)
