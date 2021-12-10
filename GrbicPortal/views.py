from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'GrbicPortal/index.html')


def employees(request):
    return render(request, 'GrbicPortal/employees.html')
