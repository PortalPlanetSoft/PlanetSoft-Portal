from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("workers/", views.workersList.as_view(), name='workers'),
]