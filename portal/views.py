from django.shortcuts import render
from portal.models import Employee
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .forms import AddEmployee
from django.http import HttpResponse


# Create your views here.
def test(request):
    return render(request, 'portal/homepage.html')

def homepage(request):
    return render(request, 'portal/homepage.html')

class workersList(ListView):
    template_name = "portal/workersList.html"
    model = Employee

class addEmployee(CreateView):
    model = Employee
    form_class = AddEmployee
    template_name = "portal/add.html"
    success_url = '/workers/'

class editEmployee(UpdateView):
    model = Employee
    form_class = AddEmployee
    template_name = "portal/add.html"
    success_url = '/workers/'



