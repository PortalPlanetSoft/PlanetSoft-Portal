from django.db import models

from users.models import User


class NewsArticle(models.Model):
    headline = models.CharField(max_length=128)
    content = models.TextField(max_length=1024)
    creation_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True,)
    likes = models.ManyToManyField(User, related_name='likes_dislikes', through='LikeDislike')


class Comment(models.Model):
    content = models.TextField(max_length=256)
    creation_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)


class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    type = models.BooleanField(null=True)
