from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Employee


def index(request):
    return render(request, 'portal/index.html')


class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'all_employees'
    template_name = 'portal/employees.html'


