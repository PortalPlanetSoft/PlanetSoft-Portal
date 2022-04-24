from django.contrib.auth.decorators import login_required
from django.urls import path

from dms import views
from dms.views import RootFolder, CreateFile, CreateFolder, UpdateFile, UpdateFolder, DeleteFile, DeleteFolder

urlpatterns = [
    path('', login_required(RootFolder.as_view()), name='dms'),
    path('create/', login_required(CreateFile.as_view()), name='create_file'),
    path('create_folder/', login_required(CreateFolder.as_view()), name='create_folder'),
    path('edit/<int:pk>', login_required(UpdateFile.as_view()), name='update_file'),
    path('edit_folder/<int:pk>', login_required(UpdateFolder.as_view()), name='update_folder'),
    path('delete/<int:pk>', login_required(DeleteFile.as_view()), name='delete_file'),
    path('delete_folder/<int:pk>', login_required(DeleteFolder.as_view()), name='delete_folder'),
    path('<str:name>/', views.get_files, name='dms'),
]
