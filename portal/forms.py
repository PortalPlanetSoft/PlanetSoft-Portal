from django.utils.translation import gettext_lazy as _
from django import forms

from users.models import CompanyPosition
from .models import User

HELP_MESSAGES = {
    'username': 'The username can contains letters, digits and @/./+/-/_.',
    'first_name': 'The first name',
}


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
    use_required_attribute = False
    first_name = forms.CharField(max_length=150, min_length=3)
    last_name = forms.CharField(max_length=150, min_length=3)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=User.GENDER_CHOICES)
    gender.required = False
    work_location = forms.ChoiceField(widget=forms.RadioSelect, choices=User.WORK_LOCATION)
    field_order = ['username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position',
                   'work_location', 'is_admin', 'is_editor']

    class Meta:
        model = User
        fields = {'username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position',
                  'work_location', 'is_admin', 'is_editor', 'profile_pic'}
        help_texts = {
            "username": None,
        }

        error_messages = ERROR_MESSAGES

        labels = {
            'is_admin': _('Admin'),
            'is_editor': _('Editor'),
            'profile_pic': _('Avatar'),
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'}),
            'company_position': forms.Select(choices=(CompanyPosition.objects.all())),
            'is_admin': forms.CheckboxInput(attrs={'label': 'Admin'}),
            'is_editor': forms.CheckboxInput(attrs={'label': 'Editor'}),
        }

    def save(self, commit=True):
        user = super(AddEmployeeForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EditEmployeeForm(forms.ModelForm):
    use_required_attribute = False
    first_name = forms.CharField(max_length=150, min_length=3)
    last_name = forms.CharField(max_length=150, min_length=3)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=User.GENDER_CHOICES)
    gender.required = False
    work_location = forms.ChoiceField(widget=forms.RadioSelect, choices=User.WORK_LOCATION)
    field_order = ['username', 'first_name', 'last_name', 'email', 'gender', 'company_position', 'work_location',
                   'is_admin', 'is_editor']

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'gender', 'company_position', 'work_location',
                  'is_admin', 'is_editor', 'profile_pic'}

        help_texts = {
            "username": None,
        }

        error_messages = ERROR_MESSAGES

        labels = {
            'is_admin': _('Admin'),
            'is_editor': _('Editor'),
            'profile_pic': _('Avatar'),
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'company_position': forms.Select(choices=(CompanyPosition.objects.all())),
            'is_admin': forms.CheckboxInput(attrs={'label': 'Admin'}),
            'is_editor': forms.CheckboxInput(attrs={'label': 'Editor'}),
        }
