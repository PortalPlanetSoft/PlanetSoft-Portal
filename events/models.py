from django.db import models

from users.models import User


class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    shared = models.ManyToManyField(to=User, related_name='shared')
    event_title = models.CharField(max_length=50)
    details = models.CharField(max_length=256, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    repeat_days = models.IntegerField(default=0, null=True, blank=True)
    repeat_every_year = models.BooleanField(default=False)
    event_type = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self
