from django.db import models


class Folder(models.Model):
    parent = models.ForeignKey('Folder', null=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)


class File(models.Model):
    parent = models.ForeignKey(Folder, null=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    extension = models.CharField(max_length=3)
