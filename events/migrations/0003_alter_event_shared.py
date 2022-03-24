# Generated by Django 4.0 on 2022-03-22 21:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_alter_event_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='shared',
            field=models.ManyToManyField(blank=True, related_name='shared', to=settings.AUTH_USER_MODEL),
        ),
    ]
