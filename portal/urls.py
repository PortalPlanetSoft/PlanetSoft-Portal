from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.users, name='all_users'),
    path('users/create/', views.user_create, name='create_user'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/edit', views.user_edit, name='user_edit'),
    path('users/', views.user_delete, name='user_delete'),
    path('', views.HomePage.as_view(), name='index'),
]