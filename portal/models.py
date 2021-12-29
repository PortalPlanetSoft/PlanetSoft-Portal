from django.db import models

from users.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
