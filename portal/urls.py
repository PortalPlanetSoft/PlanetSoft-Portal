from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("employee/", views.EmployeeList.as_view(), name="employee"),
    path("add", views.AddEmployee.as_view(), name="add"),
]
