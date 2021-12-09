from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("workers/", views.workersList.as_view(), name='workers'),
    path("add/", views.addEmployee.as_view(), name='add'),
    path("edit/<int:pk>", views.editEmployee.as_view(), name='add'),

]