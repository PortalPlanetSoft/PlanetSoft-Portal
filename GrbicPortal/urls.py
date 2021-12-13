from django.urls import path

from . import views

app_name= 'GrbicPortal'

urlpatterns = [
    path('', views.index, name='indexData'),
    path('employees/', views.AllEmployeesListView.as_view(), name='employeesData'),
]