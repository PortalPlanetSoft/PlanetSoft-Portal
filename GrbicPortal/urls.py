from django.urls import path

from . import views

app_name= 'GrbicPortal'

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees')
]