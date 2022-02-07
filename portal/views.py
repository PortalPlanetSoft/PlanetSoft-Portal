from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, ListView, DeleteView
from portal.forms import AddEmployeeForm, EditEmployeeForm
from users.models import User


class HomePage(TemplateView):
    template_name = 'portal/templates/homepage.html'


class EmployeeList(ListView):
    template_name = 'portal/templates/employee/employees.html'
    model = User
    success_url = '/employees/'


class EmployeeDetail(DetailView):
    model = User
    template_name = 'portal/templates/employee/employee-detail.html'
    context_object_name = 'employee'


class EmployeeCreate(CreateView):
    model = User
    template_name = 'portal/templates/employee/employee-create.html'
    success_url = '/employees/'
    form_class = AddEmployeeForm


class EmployeeUpdate(UpdateView):
    model = User
    template_name = 'portal/templates/employee/employee-create.html'
    success_url = '/employees/'
    form_class = EditEmployeeForm


class EmployeeDelete(DeleteView):
    model = User
    success_url = '/employees/'
    template_name = 'portal/templates/employee/employee-confirm-deletion.html'
