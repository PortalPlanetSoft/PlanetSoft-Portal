from datetime import date, datetime

from django import forms

from events.constants import LABEL_TEXT_EVENT
from events.models import Event
from users.models import User


class CreateEvent(forms.ModelForm):
    use_required_attribute = False
    field_order = ['title', 'details', 'start_time', 'end_time', 'repeat_days', 'repeat_every_year']
    shared = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all(),
                                            required=False)
    start_time = forms.DateTimeField(widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'},
                                                                      time_attrs={'type': 'time'}))
    end_time = forms.DateTimeField(widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'},
                                                                    time_attrs={'type': 'time'}))

    class Meta:
        model = Event
        fields = {'title', 'details', 'shared', 'start_time', 'end_time', 'type', 'repeat_days', 'repeat_every_year'}

    def clean_birth_date(self):
        data = self.cleaned_data['start_time']
        if data and data < date.today():
            raise forms.ValidationError('Ne možete kreirati događaj u prošlosti.')
        return data

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
