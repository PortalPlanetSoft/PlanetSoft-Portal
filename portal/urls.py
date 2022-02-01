from django.urls import path

from . import views
from .views import UserDetailView, UserCreateView, UserUpdateView, Users

urlpatterns = [
    path('users/', Users.as_view(), name='users'),
    path('users/create/', UserCreateView.as_view(), name='create-user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/edit', UserUpdateView.as_view(), name='user-edit'),
    path('users/<int:pk>/delete', views.user_delete, name='user-delete'),
    path('', views.HomePage.as_view(), name='index'),
]
