from django import forms

from events.constants import LABEL_TEXT_EVENT
from events.models import Event
from users.models import User


class CreateEvent(forms.ModelForm):
    use_required_attribute = False
    field_order = ['title', 'details', 'start_time', 'end_time', 'repeat_days', 'repeat_every_year']
    shared = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all(),
                                            required=False)

    class Meta:
        model = Event
        fields = {'title', 'details', 'shared', 'start_time', 'end_time', 'type', 'repeat_days', 'repeat_every_year'}

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
        for key, value in LABEL_TEXT_EVENT.items():
            self.fields[key].label = value
