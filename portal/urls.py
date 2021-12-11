from django.urls import path

from . import views

app_name= 'portal'

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.EmployeeListView.as_view(), name='employees')
]