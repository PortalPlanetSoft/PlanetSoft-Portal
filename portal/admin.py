from django.contrib import admin
from .models import Employee, CompanyPosition, Department

admin.site.register(Employee)
admin.site.register(CompanyPosition)
admin.site.register(Department)
