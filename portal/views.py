from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView

from portal.forms import AddEditUserForm
from users.models import User


class HomePage(TemplateView):
    template_name = "portal/templates/homepage.html"


class Users(TemplateView):
    template_name = 'portal/templates/user/users.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'portal/templates/user/user-detail.html'
    context_object_name = 'user'


class UserCreateView(CreateView):
    model = User
    template_name = 'portal/templates/user/user-create.html'
    success_url = '/users/'
    form_class = AddEditUserForm


class UserUpdateView(UpdateView):
    model = User
    template_name = 'portal/templates/user/user-create.html'
    success_url = '/users/'
    form_class = AddEditUserForm


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = False
    #user.save()
    user.delete()
    return redirect('users')
