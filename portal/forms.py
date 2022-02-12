from django import forms

from users.models import CompanyPosition
from .models import User


CHOICES = [('True', 'Female'), ('False', 'Male')]
ERROR_MESSAGES = {
    'username': {
        'unique': "This username is already taken.",
        'invalid': "The username can contain letters, digits and @/./+/-/_ only.",
        'max_length': "This username is too long.",
        'required': "This field is required.",
    },
    'first_name': {
        'max_length': "This first name is too long.",
        'min_length': "This first name is too short.",
        'required': "This field is required.",
    },
    'last_name': {
        'max_length': "This last name is too long.",
        'min_length': "This last name is too short.",
        'required': "This field is required.",
    },
    'email': {
        'invalid': "Please enter a valid email address.",
        'unique': "This email address is already used.",
        'required': "This field is required.",
    },
    'company_position': {
        'max_length': "This first name is too long.",
        'required': "This field is required.",
    },
}


class AddEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, min_length=3)
    last_name = forms.CharField(max_length=150, min_length=3)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    gender.required = False
    field_order = ['username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position']

    class Meta:
        model = User
        fields = {'username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position'}
        help_texts = {
            "username": None,
        }

        error_messages = ERROR_MESSAGES

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'}),
            'company_position': forms.Select(choices=(CompanyPosition.objects.all()))
        }

    def save(self, commit=True):
        user = super(AddEmployeeForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EditEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, min_length=3)
    last_name = forms.CharField(max_length=150, min_length=3)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    gender.required = False
    field_order = ['username', 'first_name', 'last_name', 'email', 'gender', 'company_position']

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'gender', 'company_position'}

        help_texts = {
            "username": None,
        }

        error_messages = ERROR_MESSAGES

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'company_position': forms.Select(choices=(CompanyPosition.objects.all()))
        }
