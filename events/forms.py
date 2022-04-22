from datetime import datetime, timezone

from django import forms

from events.constants import LABEL_TEXT_EVENT
from events.models import Event
from users.models import User


class CreateEvent(forms.ModelForm):
    use_required_attribute = False
    field_order = ['title', 'details', 'start_time', 'end_time', 'repeat_days', 'repeat_every_year']
    shared = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all(),
                                            required=False)
    start_time = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'},
                                                                           time_attrs={'type': 'time'}))
    end_time = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'},
                                                                         time_attrs={'type': 'time'}), required=False)

    class Meta:
        model = Event
        fields = {'title', 'details', 'shared', 'type', 'start_time', 'end_time', 'repeat_days', 'repeat_every_year'}

    def save(self, commit=True):
        event = super(CreateEvent, self).save(commit=True)
        # todo ovdje implementirati task scheduler na osnovu odabranog unosa
        if commit:
            event.save()
        return event

    def clean_start_time(self):
        data = self.cleaned_data['start_time']
        if data and data < datetime.now(timezone.utc).astimezone():
            raise forms.ValidationError('Događaj ne može počinjati u prošlosti')
            datetime.now(pytz.utc)
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in LABEL_TEXT_EVENT.items():
            self.fields[key].label = value
