from django import forms

from users.models import CompanyPosition
from .models import User


CHOICES = [('1', 'Female'), ('0', 'Male')]


class AddEmployeeForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    field_order = ['username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position']

    class Meta:
        model = User
        fields = {'username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position'}

        help_texts = {
            "username": None,
        }

        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.TextInput(),
            'company_position': forms.Select(choices=(CompanyPosition.objects.all()))
        }

    def save(self, commit=True):
        user = super(AddEmployeeForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EditEmployeeForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    field_order = ['username', 'first_name', 'last_name', 'email', 'gender', 'company_position']

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'gender', 'company_position'}

        help_texts = {
            "username": None,
        }

        widgets = {
            'username': forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.TextInput(),
            'company_position': forms.Select(choices=(CompanyPosition.objects.all()))
        }
