from django import forms

from users.models import CompanyPosition
from .models import User


class AddEditUserForm(forms.ModelForm):
    CHOICES = [('1', 'Female'), ('0', 'Male')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    field_order = ['username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position']

    class Meta:
        model = User
        fields = {'username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position'}

        # stavis umjesto css-klasa naziv svoje css klase i izmjenice izgled ovih polja
        widgets = {
            'username': forms.TextInput(attrs={'class': 'css-klasa'}),
            'password': forms.PasswordInput(attrs={'class': 'css-klasa'}),
            'first_name': forms.TextInput(attrs={'class': 'css-klasa'}),
            'last_name': forms.TextInput(attrs={'class': 'css-klasa1'}),
            'email': forms.TextInput(attrs={'class': 'css-klasa'}),
            'company_position': forms.Select(attrs={'class': 'css-klasa'}, choices=(CompanyPosition.objects.all()))
        }

    def save(self, commit=True):
        user = super(AddEditUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
