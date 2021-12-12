from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.EmployeeView.as_view(), name='employees')
]
