from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import EmployeeCreate, EmployeeUpdate, EmployeeList, EmployeeDelete, Profile

urlpatterns = [
    path('profile/', login_required(Profile.as_view()), name='profile'),
    path('employees/', login_required(EmployeeList.as_view()), name='employees'),
    path('employees/create/', login_required(EmployeeCreate.as_view()), name='employee-create'),
    path('employees/<int:pk>/', login_required(EmployeeUpdate.as_view()), name='employee-edit'),
    path('employees/delete/<int:pk>/', login_required(EmployeeDelete.as_view()), name='employee-delete'),
]
