from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, FormView

from praksaPlanetSoft.constants import FIRST_PAGE, HTTP_STATUS_400, HTTP_STATUS_401, HTTP_STATUS_200
from users.constants import USER_CARDS_PER_PAGE
from users.forms import AddEmployeeForm, EditEmployeeForm, ProfileForm
from users.models import User, CompanyPosition


class EmployeeList(ListView):
    template_name = 'users/employee/employees.html'
    model = User
    success_url = '/employees/'
    paginate_by = USER_CARDS_PER_PAGE

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)

        page = self.request.GET.get('page', FIRST_PAGE)
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


class EmployeeCreate(UserPassesTestMixin, CreateView):
    model = User
    template_name = 'users/employee/employee-create.html'
    success_url = '/employees/'
    form_class = AddEmployeeForm

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = HTTP_STATUS_400
        return response

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser:
            return True
        else:
            raise PermissionDenied("You are not authorized to add new employees")


# acts like UpdateView when user is admin or superuser
# and is preview view if user is none of above
class EmployeeUpdate(UpdateView):
    model = User
    template_name = 'users/employee/employee-edit.html'
    success_url = '/employees/'
    form_class = EditEmployeeForm

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdate, self).get_context_data(**kwargs)
        context["object_id"] = self.kwargs["pk"]
        if not self.request.POST:
            if self.request.user.is_superuser or self.request.user.is_admin:
                context['form'] = EditEmployeeForm(instance=context['object'])
            else:
                context['form_preview'] = EditEmployeeForm(instance=context['object'], disable_fields=True)
        return context

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = HTTP_STATUS_400
        return response


class EmployeeDelete(UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/employees/'
    template_name = 'users/employee/employee-confirm-deletion.html'

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser:
            return True
        elif self.request.user.is_authenticated:
            raise PermissionDenied("You are not authorized to delete employees")
        raise


class Profile(UpdateView, FormView):
    template_name = 'users/employee/profile.html'
    form_class = ProfileForm
    model = User
    success_url = '/employees/profile/'

    def get_object(self, queryset=None):
        return User.objects.filter(pk=self.request.user.id).first()


class PasswordChange(PasswordChangeView):
    success_url = '/logout/'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=HTTP_STATUS_401)


@login_required
def remove_avatar(request):

        User.objects.filter(id=request.user.id).first().profile_pic.delete(save=True)
        return HTTP_STATUS_200
