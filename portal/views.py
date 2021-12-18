from django.shortcuts import render
from django.views.generic import ListView, CreateView

from portal.forms import AddEmployee
from portal.models import Employee


def home(request):
    return render(request, 'portal/home.html')


class EmployeeList(ListView):
    template_name = "portal/employee.html"
    model = Employee

class AddEmployee(CreateView):
    template_name = "portal/addEmployee.html"
    form_class = AddEmployee
    model = Employee
    success_url = "/employee"

