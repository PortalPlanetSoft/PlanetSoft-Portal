from django.shortcuts import render

from django.views import generic
from . models import Employee

def index(request):
    return render(request, 'index/index.html')

class EmployeeView(generic.ListView):
    model = Employee
    template_name = 'index/employees.html'
    context_object_name = 'employee_list'