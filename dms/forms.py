from django import forms

from dms.models import File, Folder


class FileForm(forms.ModelForm):
    use_required_attribute = False
    field_order = ['name', 'parent', 'file']

    class Meta:
        model = File
        fields = {'parent', 'name', 'file'}


class FolderForm(forms.ModelForm):
    use_required_attribute = False
    field_order = ['name', 'parent']

    class Meta:
        model = Folder
        fields = {'parent', 'name'}

