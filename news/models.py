from django.db import models

from users.models import User


class NewsArticle(models.Model):
    headline = models.CharField(max_length=128)
    content = models.TextField(max_length=1024)
    creation_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField(max_length=256)
    creation_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
