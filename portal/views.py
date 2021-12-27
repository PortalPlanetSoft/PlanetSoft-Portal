from django.shortcuts import render
from portal.models import Employee
from django.views.generic.list import ListView


# Create your views here.
def test(request):
    return render(request, 'portal/homepage.html')


def homepage(request):
    return render(request, 'portal/homepage.html')


class workersList(ListView):
    template_name = "portal/workersList.html"
    model = Employee

