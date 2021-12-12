from django.contrib import admin

from .models import Sector, Position, Employee

# Register your models here.
admin.site.register(Sector)
admin.site.register(Position)
admin.site.register(Employee)
