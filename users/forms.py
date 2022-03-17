from datetime import date

from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.utils.translation import gettext_lazy as _
from django import forms
import re

from users.models import CompanyPosition

HELP_MESSAGES = {
    'username': 'The username can contains letters, digits and @/./+/-/_.',
    'first_name': 'The first name',
}

REGEX_PHONE_NUMBER = "(\+387|00387|0)(66|65|61)[0-9]{6}$"

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

LABEL_TEXT = {
    'username': _('Korisničko ime'),
    'first_name': _('Ime'),
    'last_name': _('Prezime'),
    'gender': _('Pol'),
    'email': _('Email adresa'),
    'company_position': _('Pozicija u kompaniji'),
    'work_location': _('Radno mjesto'),
    'is_admin': _('Admin'),
    'is_editor': _('Editor'),
    'profile_pic': _('Avatar'),
    'birth_date': _('Datum rođenja'),
    'phone': _('Broj telefona'),
    'business_phone': _('Poslovni broj telefona'),
}
EMPLOYEE_LABEL_TEXT = {
    'username': _('Korisničko ime'),
    'first_name': _('Ime'),
    'last_name': _('Prezime'),
    'gender': _('Pol'),
    'email': _('Email adresa'),
    'company_position': _('Pozicija u kompaniji'),
    'work_location': _('Radno mjesto'),
    'is_admin': _('Admin'),
    'is_editor': _('Editor'),
    'birth_date': _('Datum rođenja'),
    'phone': _('Broj telefona'),
    'business_phone': _('Poslovni broj telefona'),
}
PROFILE_LABEL_TEXT = {
    'first_name': _('Ime'),
    'last_name': _('Prezime'),
    'email': _('Email adresa'),
    'profile_pic': _('Avatar'),
    'birth_date': _('Datum rođenja'),
    'phone': _('Broj telefona'),
    'business_phone': _('Poslovni broj telefona'),
}


class AddEmployeeForm(forms.ModelForm):
    use_required_attribute = False
    first_name = forms.CharField(max_length=150, min_length=3)
    last_name = forms.CharField(max_length=150, min_length=3)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=User.GENDER_CHOICES)
    gender.required = False
    work_location = forms.ChoiceField(widget=forms.RadioSelect, choices=User.WORK_LOCATION)

    field_order = ['username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position',
                   'work_location', 'is_admin', 'is_editor', 'birth_date', 'phone', 'business_phone']

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        current = date.today()
        if data and data.year > current.year - 18:
            raise forms.ValidationError('Date can\'t be newer than 18 years of current year')
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if data and not bool(re.match(REGEX_PHONE_NUMBER, data)):
            raise forms.ValidationError('Phone number format wrong!')
        return data

    def clean_business_phone(self):
        data = self.cleaned_data['business_phone']
        if data and not bool(re.match(REGEX_PHONE_NUMBER, data)):
            raise forms.ValidationError('Phone number format wrong!')
        return data

    class Meta:
        model = User
        fields = {'username', 'password', 'first_name', 'last_name', 'email', 'gender', 'company_position',
                  'work_location', 'is_admin', 'is_editor', 'birth_date', 'phone', 'business_phone'}
        help_texts = {
            "username": None,
        }
        error_messages = ERROR_MESSAGES
        labels = LABEL_TEXT

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Korisničko ime'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Lozinka'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ime'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Prezime'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email adresa'}),
            'company_position': forms.Select(choices=(CompanyPosition.objects.all())),
            'is_admin': forms.CheckboxInput(attrs={'label': 'Admin'}),
            'is_editor': forms.CheckboxInput(attrs={'label': 'Editor'}),
            'birth_date': forms.DateInput(attrs={'placeholder': 'Datum rođenja', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Broj telefona'}),
            'business_phone': forms.TextInput(attrs={'placeholder': 'Poslovni broj telefona'})
        }

    def save(self, commit=True):
        user = super(AddEmployeeForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in EMPLOYEE_LABEL_TEXT.items():
                self.fields[key].label = value
        self.fields['first_name'].placeholder = "Ime"


class EditEmployeeForm(forms.ModelForm):
    use_required_attribute = False
    first_name = forms.CharField(max_length=150, min_length=3)
    last_name = forms.CharField(max_length=150, min_length=3)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=User.GENDER_CHOICES)
    gender.required = False
    work_location = forms.ChoiceField(widget=forms.RadioSelect, choices=User.WORK_LOCATION)
    field_order = ['username', 'first_name', 'last_name', 'email', 'gender', 'company_position', 'work_location',
                   'is_admin', 'is_editor', 'birth_date', 'phone', 'business_phone']

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        current = date.today()
        if data and data.year > current.year - 18:
            raise forms.ValidationError('Date can\'t be newer than 18 years of current year')
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if data and not bool(re.match(REGEX_PHONE_NUMBER, data)):
            raise forms.ValidationError('Phone number format wrong!')
        return data

    def clean_business_phone(self):
        data = self.cleaned_data['business_phone']
        if data and not bool(re.match(REGEX_PHONE_NUMBER, data)):
            raise forms.ValidationError('Phone number format wrong!')
        return data

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'gender', 'company_position', 'work_location',
                  'is_admin', 'is_editor', 'birth_date', 'phone', 'business_phone'}

        help_texts = {
            "username": None,
        }
        error_messages = ERROR_MESSAGES
        labels = LABEL_TEXT

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Korisničko ime'}),
            # todo provjerite zasto ne radi labela za ime i prezime i pol
            'first_name': forms.TextInput(attrs={'placeholder': 'Ime', 'label': 'OVO JE LABEL ZA IME'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Prezime'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'company_position': forms.Select(choices=(CompanyPosition.objects.all())),
            'is_admin': forms.CheckboxInput(attrs={'label': 'Admin'}),
            'is_editor': forms.CheckboxInput(attrs={'label': 'Editor'}),
            'birth_date': forms.DateInput(attrs={'placeholder': 'Datum rođenja', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Broj telefona'}),
            'business_phone': forms.TextInput(attrs={'placeholder': 'Poslovni broj telefona'})
        }

    def __init__(self, disable_fields=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in EMPLOYEE_LABEL_TEXT.items():
                self.fields[key].label = value
        if disable_fields:
            self.fields['username'].disabled = True
            self.fields['first_name'].disabled = True
            self.fields['last_name'].disabled = True
            self.fields['email'].disabled = True
            self.fields['gender'].disabled = True
            self.fields['company_position'].disabled = True
            self.fields['work_location'].disabled = True
            self.fields['is_admin'].disabled = True
            self.fields['is_editor'].disabled = True
            self.fields['business_phone'].disabled = True
            self.fields['phone'].disabled = True
            self.fields['birth_date'].disabled = True


class ProfileForm(forms.ModelForm):
    use_required_attribute = False
    first_name = forms.CharField(max_length=150, min_length=3)
    last_name = forms.CharField(max_length=150, min_length=3)
    profile_pic = forms.ImageField(label=_('Avatar'), required=False, widget=forms.FileInput)
    field_order = ['first_name', 'last_name', 'email', 'birth_date', 'phone', 'business_phone', 'profile_pic']

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        current = date.today()
        if data and data.year > current.year - 18:
            raise forms.ValidationError('Date can\'t be newer than 18 years of current year')
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if data and not bool(re.match(REGEX_PHONE_NUMBER, data)):
            raise forms.ValidationError('Phone number format wrong!')
        return data

    def clean_business_phone(self):
        data = self.cleaned_data['business_phone']
        if data and not bool(re.match(REGEX_PHONE_NUMBER, data)):
            raise forms.ValidationError('Phone number format wrong!')
        return data

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'profile_pic', 'birth_date', 'phone', 'business_phone'}
        error_messages = ERROR_MESSAGES

        labels = {
            'profile_pic': _('Avatar'),
            'birth_date': _('Datum rođenja'),
            'phone': _('Broj telefona'),
            'business_phone': _('Poslovni broj telefona'),
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ime'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Prezime'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'birth_date': forms.DateInput(attrs={'placeholder': 'Datum rođenja', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Broj telefona'}),
            'business_phone': forms.TextInput(attrs={'placeholder': 'Poslovni broj telefona'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in PROFILE_LABEL_TEXT.items():
                self.fields[key].label = value


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
