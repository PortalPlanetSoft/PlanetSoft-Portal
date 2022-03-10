# Generated by Django 4.0 on 2022-03-05 15:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_newsarticle_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='dislikes',
            field=models.ManyToManyField(related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
