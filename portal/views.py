from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from users.models import User


class HomePage(TemplateView):
    template_name = "portal/templates/homepage.html"


def users(request):
    if request.method == 'POST':
        pass
        # todo sacuvaj novog korisnika
    return render(request, 'portal/templates/employees.html', {'users': User.objects.filter(is_active=True)})


def user_create(request):
    return render(request, 'portal/templates/employeeCreate.html')


def user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'portal/templates/employeeCreate.html', {'user': user})


def user_detail(request, user_id):
    if request.method == 'POST':
        pass
        # todo update korisnika
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'portal/templates/employeeDetails.html', {'user': user})


def user_delete(request):
    user = get_object_or_404(User, pk=user_id)#todo ne moze user_id mora iz post-a id polje
    user.is_active = False
    return render(request, 'portal/templates/employees.html', {'users': User.objects.filter(is_active=True)})
