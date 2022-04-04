from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import EmployeeCreate, EmployeeUpdate, EmployeeList, EmployeeDelete, Profile, PasswordChange, \
    remove_avatar, LoginNotification, previous_login

urlpatterns = [
    path('', login_required(EmployeeList.as_view()), name='employees'),
    path('notification', login_required(LoginNotification.as_view()), name='notification'),
    path('create/', login_required(EmployeeCreate.as_view()), name='employee-create'),
    path('<int:pk>/', login_required(EmployeeUpdate.as_view()), name='employee-edit'),
    path('delete/<int:pk>/', login_required(EmployeeDelete.as_view()), name='employee-delete'),
    path('profile/', login_required(Profile.as_view()), name='profile'),
    path('password-change/', login_required(PasswordChange.as_view(
        template_name='users/authentication/password_change.html')), name='password-change'),
    path('remove-avatar/', remove_avatar, name='remove-avatar'),
    path('previous-login/', previous_login, name='previous-login'),
]
