from django import forms

from events.models import Event


class CreateEvent(forms.ModelForm):
    use_required_attribute = False
    field_order = ['title', 'details',  'shared', 'start_time', 'end_time', 'repeat_days', 'repeat_every_year']

    class Meta:
        model = Event
        fields = {'title', 'details',  'shared',  'start_time', 'end_time', 'repeat_days', 'repeat_every_year'}

        widgets = {
            'start_time': forms.DateInput(attrs={'placeholder': 'Datum početka događaja', 'type': 'date'})
        }

    def save(self, commit=True):
        event = super(CreateEvent, self).save(commit=False)
        # todo ovdje implementirati task scheduler na osnovu odabranog unosa
        #user.set_password(self.cleaned_data["password"])
        if commit:
            event.save()
        return event

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
