from django.db import models

from events.constants import EVENT_TYPES


class Event(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    shared = models.ManyToManyField(to='users.User', related_name='shared')
    title = models.CharField(max_length=48)
    details = models.CharField(max_length=256, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    repeat_days = models.IntegerField(default=0, null=True, blank=True)
    repeat_every_year = models.BooleanField(default=False)
    type = models.CharField(max_length=20, null=True, blank=True, choices=EVENT_TYPES)

