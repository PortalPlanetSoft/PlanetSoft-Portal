from django.http import JsonResponse
from django.views.generic import TemplateView

from dms.models import Folder, File


class RootFolder(TemplateView):
    template_name = 'dms/dms.html'




def get_files(self, name):
    return JsonResponse({
        'folders': list(Folder.objects.filter(folder__name=name)),
        'files': list(File.objects.filter(folder__name=name))
    })
