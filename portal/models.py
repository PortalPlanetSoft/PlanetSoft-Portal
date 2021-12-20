from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(unique=True)


class Department(models.Model):
    department_name = models.CharField(max_length=100)

    # pitaj za problem modelovanja 1:1 Department-Employee kao sef odsjeka

    def __str__(self):
        return self.department_name


class CompanyPosition(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    position_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.position_name + ' (' + self.department.department_name + ')')


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=125)
    position = models.ForeignKey(CompanyPosition, on_delete=models.CASCADE)
    time_joined = models.DateField(null=True, blank=True)
    office_number = models.PositiveIntegerField(null=True, blank=True, )

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)
