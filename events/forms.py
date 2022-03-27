from django import forms
from django.db import transaction

from events.models import Event
from users.models import User


class CreateEvent(forms.ModelForm):
    use_required_attribute = False
    field_order = ['title', 'details', 'start_time', 'end_time', 'repeat_days', 'repeat_every_year']
    shared = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all())

    class Meta:
        model = Event
        fields = {'title', 'details', 'shared', 'start_time', 'end_time', 'repeat_days', 'repeat_every_year'}

        widgets = {
            'start_time': forms.DateTimeInput(attrs={'placeholder': 'GGGG-MM-DD/SS:MM'}),
            'end_time': forms.DateTimeInput(attrs={'placeholder': 'GGGG-MM-DD/SS:MM'}),
        }

    def save(self, commit=True):
        event = super(CreateEvent, self).save(commit=True)
        # todo ovdje implementirati task scheduler na osnovu odabranog unosa
        if commit:
            event.save()
        return event

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
