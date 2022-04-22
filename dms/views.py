from django.core import serializers
from django.http import HttpResponse
from django.views.generic import TemplateView

from dms.models import Folder, File


class RootFolder(TemplateView):
    template_name = 'dms/dms.html'


def get_files(self, name):
    data = list(File.objects.filter(parent__name=name))
    data.extend(list(Folder.objects.filter(parent__name=name)))
    data = serializers.serialize('json', data)
    return HttpResponse(data, content_type='application/json')
