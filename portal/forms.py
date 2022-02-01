from django import forms

from users.models import CompanyPosition
from .models import User


class AddEditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position'}

        # stavis umjesto css-klasa naziv svoje css klase i izmjenice izgled ovih polja
        widgets = {
            'username': forms.TextInput(attrs={'class': 'css-klasa'}),
            'password': forms.TextInput(attrs={'class': 'css-klasa'}),
            'first_name': forms.TextInput(attrs={'class': 'css-klasa'}),
            'last_name': forms.TextInput(attrs={'class': 'css-klasa1'}),
            'email': forms.TextInput(attrs={'class': 'css-klasa'}),
            'gender': forms.CheckboxInput(attrs={'class': 'css-klasa'}),
            'company_position': forms.Select(attrs={'class': 'css-klasa'}, choices=(CompanyPosition.objects.all()))
        }
