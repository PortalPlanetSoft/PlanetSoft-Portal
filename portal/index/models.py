from django.db import models

class Sector(models.Model):
    sector_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sector_name

class Position(models.Model):
    position_name = models.CharField(max_length=50)
    sector_name = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.position_name

class Employee(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return (f" {self.first_name} {self.last_name}")

