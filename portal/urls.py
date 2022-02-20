from django.urls import path

from . import views
from .views import EmployeeCreate, EmployeeUpdate, EmployeeList, EmployeeDelete, Profile

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('profile/', Profile.as_view(), name='profile'),
    path('employees/', EmployeeList.as_view(), name='employees'),
    path('employees/create/', EmployeeCreate.as_view(), name='employee-create'),
    path('employees/<int:pk>/', EmployeeUpdate.as_view(), name='employee-edit'),
    path('employees/<int:pk>/', EmployeeDelete.as_view(), name='employee-delete'),
]
