from django.db import models


class Folder(models.Model):
    parent = models.ForeignKey('Folder', null=True, blank=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=False, blank=False)


class File(models.Model):
    parent = models.ForeignKey(Folder, null=True, blank=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=False, blank=False)
    extension = models.CharField(max_length=10)
    file = models.FileField(upload_to='files')
