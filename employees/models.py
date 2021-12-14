from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    title = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name + " " + self.surname
