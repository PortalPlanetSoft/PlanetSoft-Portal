from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView, FormView

from portal.forms import AddEmployeeForm, EditEmployeeForm, ProfileForm
from users.models import User, CompanyPosition

'''class HomePage(TemplateView):
    template_name = 'portal/templates/homepage.html'
'''


class EmployeeList(ListView):
    template_name = 'portal/templates/employee/employees.html'
    model = User
    success_url = '/employees/'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)

        page = self.request.GET.get('page', 1)
        users = self.object_list.order_by('first_name', 'last_name')
        paginator = self.paginator_class(users, self.paginate_by)
        users = paginator.page(page)

        # parametar pozicije u kompaniji za GET request
        if self.request.GET.get('position'):
            if self.request.GET.get('position') == 'all':
                context['selected'] = self.request.GET.get('position')
            else:
                context['selected'] = int('0' + self.request.GET.get('position'))

        # parametar pretrage za GET request
        if self.request.GET.get('search'):
            context['search'] = self.request.GET.get('search')

        # parametar lokacije za GET request
        if self.request.GET.get('location'):
            context['location'] = self.request.GET.get('location')

        context['position'] = self.request.GET.get('position')
        context['object_list'] = users
        context['position_list'] = CompanyPosition.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        query_set = super().get_queryset()
        search = self.request.GET.get('search')
        position = self.request.GET.get('position')
        location = self.request.GET.get('location')
        if search:
            filtered_query = query_set.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
            if len(filtered_query) == 0:
                query_set = query_set.filter(company_position__position_name__icontains=search)
            else:
                query_set = filtered_query

        if position and position != 'all':
            query_set = query_set.filter(Q(company_position__id__exact=position))

        if location and location != 'all':
            query_set = query_set.filter(Q(work_location__exact=location))
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
            raise PermissionDenied("You are not authorized to add new employees")


class EmployeeUpdate(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'portal/templates/employee/employee-edit.html'
    success_url = '/employees/'
    form_class = EditEmployeeForm

    def get_context_data(self, **kwargs):
        ctx = super(EmployeeUpdate, self).get_context_data(**kwargs)
        ctx["object_id"] = self.kwargs["pk"]
        return ctx

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser:
            return True
        else:
            raise PermissionDenied("You are not authorized to edit employees")


class EmployeeDelete(UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/employees/'
    template_name = 'portal/templates/employee/employee-confirm-deletion.html'

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser:
            return True
        elif self.request.user.is_authenticated:
            raise PermissionDenied("You are not authorized to delete employees")
        raise


class Profile(UpdateView, FormView):
    template_name = 'portal/templates/authentication/profile.html'
    form_class = ProfileForm
    model = User
    success_url = '/profile/'

    def get_object(self, queryset=None):
        return User.objects.filter(pk=self.request.user.id).first()


class Preview(DetailView):
    template_name = 'portal/templates/employee/employee-edit.html'

    def get_object(self, queryset=None):
        return User.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(Preview, self).get_context_data(**kwargs)
        # todo pitaj ovo
        ''' todo pitaj
        base_fields = {}
        for field in form.base_fields.items():
            field[1].disabled = True
            base_fields[field[0]] = field[1]
        form.base_fields = base_fields'''
        context['form_preview'] = EditEmployeeForm(instance=context['object'].get(), disable_fields=True)
        return context


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('logout')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=401)


def error_500(request, exception=None):
    return render(request, "errors/500.html", {'error_message': exception})


def error_404(request, exception):
    return render(request, "errors/404.html", {'error_message': exception})


def error_403(request, exception=None):
    return render(request, "errors/403.html", {'error_message': exception})


def error_400(request, exception=None):
    return render(request, "errors/400.html", {'error_message': exception})
