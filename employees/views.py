from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Employee
# Create your views here.
from django.urls import path

from . import views


def index(request):
    employees_list = Employee.objects.order_by('id')
    template = loader.get_template('employees/employees.html')
    context = {
        'employees_list': employees_list,
    }
    return HttpResponse(template.render(context, request))


def home_page(request):
    template = loader.get_template('employees/naslovna.html')
    return HttpResponse(template.render(None, request))
