from django.utils.translation import gettext_lazy as _

# users/models.py

GENDER_CHOICES = [
    ('F', 'Ženski'),
    ('M', 'Muški')
]

WORK_LOCATION = [
    ('BL', 'Banja Luka'),
    ('BG', 'Beograd')
]

# users/forms.py

HELP_MESSAGES = {
    'username': 'The username can contains letters, digits and @/./+/-/_.',
    'first_name': 'The first name',
}

REGEX_PHONE_NUMBER = "^(\+387|00387|0)(66|65|61|63)[0-9]{6}$"

REGEX_BUSINESS_PHONE_NUMBER = "^[0-9]{3}$"

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

LABEL_TEXT_USER = {
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

# users/views.py
USER_CARDS_PER_PAGE = 9
