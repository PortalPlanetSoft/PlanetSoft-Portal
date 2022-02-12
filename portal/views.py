from django.db.models import Q
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, ListView, DeleteView
from portal.forms import AddEmployeeForm, EditEmployeeForm
from users.models import User


class HomePage(TemplateView):
    template_name = 'portal/templates/homepage.html'


class EmployeeList(ListView):
    template_name = 'portal/templates/employee/employees.html'
    model = User
    success_url = '/employees/'
    paginate_by = 9

    def get_queryset(self, *args, **kwargs):
        query_set = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            filtered_query = query_set.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
            if len(filtered_query) == 0:
                query_set = query_set.filter(company_position__position_name__icontains=query)
            else:
                query_set = filtered_query
        return query_set


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
