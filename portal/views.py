from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'portal/index.html')


def employees(request):
    return render(request, 'portal/employees.html')