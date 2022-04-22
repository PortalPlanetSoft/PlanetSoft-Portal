from django.core import serializers
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from dms.forms import FileForm, FolderForm
from dms.models import Folder, File


class RootFolder(TemplateView):
    template_name = 'dms/dms.html'


class CreateFile(CreateView):
    model = File
    success_url = '/dms/'
    form_class = FileForm


class CreateFolder(CreateView):
    model = Folder
    success_url = '/dms/'
    form_class = FolderForm


class UpdateFile(UpdateView):
    model = File
    success_url = '/dms/'
    form_class = FileForm


class UpdateFolder(UpdateView):
    model = Folder
    success_url = '/dms/'
    form_class = FolderForm


class DeleteFile(DeleteView):
    model = File
    success_url = '/dms/'


class DeleteFolder(DeleteView):
    model = Folder
    success_url = '/dms/'


def get_files(self, name):
    data = list(File.objects.filter(parent__name=name))
    data.extend(list(Folder.objects.filter(parent__name=name)))
    data = serializers.serialize('json', data)
    return HttpResponse(data, content_type='application/json')
