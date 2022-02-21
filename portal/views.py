from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseBadRequest, Http404
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, ListView, DeleteView
from portal.forms import AddEmployeeForm, EditEmployeeForm
from users.models import User, CompanyPosition


class HomePage(TemplateView):
    template_name = 'portal/templates/homepage.html'


class EmployeeList(ListView):
    template_name = 'portal/templates/employee/employees.html'
    model = User
    success_url = '/employees/'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)

        page = self.request.GET.get('page', 1)
        users = self.object_list
        paginator = self.paginator_class(users, self.paginate_by)
        users = paginator.page(page)
        if self.request.GET.get('position'):
            if self.request.GET.get('position') == 'all':
                context['selected'] = self.request.GET.get('position')
            else:
                context['selected'] = int('0'+self.request.GET.get('position'))
        if self.request.GET.get('search'):#todo nije najbolje za search ali okej je
            context['search'] = self.request.GET.get('search')
        context['position'] = self.request.GET.get('position')
        context['object_list'] = users
        context['position_list'] = CompanyPosition.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        query_set = super().get_queryset()
        search = self.request.GET.get('search')
        position = self.request.GET.get('position')
        if search:
            filtered_query = query_set.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
            if len(filtered_query) == 0:
                query_set = query_set.filter(company_position__position_name__icontains=search)
            else:
                query_set = filtered_query

        if position and position != 'all':
            query_set = query_set.filter(Q(company_position__id__exact=position))
        return query_set


class EmployeeDetail(DetailView):
    model = User
    template_name = 'portal/templates/employee/employee-detail.html'
    context_object_name = 'employee'


class EmployeeCreate(UserPassesTestMixin, CreateView):
    model = User
    template_name = 'portal/templates/employee/employee-create.html'
    success_url = '/employees/'
    form_class = AddEmployeeForm

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser:
            return True
        else:
            raise Http404("You are not authorized to add new employees")#todo promjeni response


class EmployeeUpdate(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'portal/templates/employee/employee-edit.html'
    success_url = '/employees/'
    form_class = EditEmployeeForm

    def get_context_data(self, **kwargs):
        ctx = super(EmployeeUpdate, self).get_context_data(**kwargs)
        ctx["object_id"]=self.kwargs["pk"]
        return ctx

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser:
            return True
        else:
            raise Http404("You are not authorized to edit employees")  # todo promjeni response


class EmployeeDelete(UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/employees/'
    template_name = 'portal/templates/employee/employee-confirm-deletion.html'

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser:
            return True
        else:
            raise Http404("You are not authorized to delete employees")  # todo promjeni response


class Profile(DetailView):
    template_name = 'portal/templates/authentication/profile.html'

    def get_object(self, queryset=None):
        return User.objects.filter(pk=self.request.user.id)
