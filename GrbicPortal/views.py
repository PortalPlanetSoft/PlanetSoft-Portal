from django.shortcuts import render
from .models import Employee
from django.views.generic.list import ListView

# Create your views here.

def index(request):
    return render(request, 'GrbicPortal/indexData.html')


#def employees(request):
 #   employeeList = Employee.objects.all()
  #  return render(request, 'GrbicPortal/employeeData.html', {{"employeeList":employeeList}})
class AllEmployeesListView(ListView):
    model = Employee
    context_object_name = 'employeesList'
    template_name = 'GrbicPortal/employeeData.html'
