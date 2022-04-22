from django.contrib.auth.decorators import login_required
from django.urls import path

from dms import views
from dms.views import RootFolder

urlpatterns = [
    path('', login_required(RootFolder.as_view()), name='dms'),
    path('<str:name>', views.get_files, name='dms'),
]
