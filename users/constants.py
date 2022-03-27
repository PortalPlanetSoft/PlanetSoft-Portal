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
    'username': 'Korisničko ime može sadržati slova, cifre i znakove @/./+/-/_.',
}

REGEX_PHONE_NUMBER = "^(\+387|00387|0)(66|65|61|63)[0-9]{6}$"

REGEX_BUSINESS_PHONE_NUMBER = "^[0-9]{3}$"

ERROR_MESSAGES = {
    'username': {
        'unique': "Korisničko ime je već u upotrebi",
        'invalid': "Korisničko ime može sadržati slova, cifre i znakove @/./+/-/_.",
        'max_length': "Korisničko ime je predugačko",
        'required': "Ovo polje je obavezno",
    },
    'first_name': {
        'max_length': "Ime je predugačko",
        'min_length': "Ime je prekratko",
        'required': "Ovo polje je obavezno",
    },
    'last_name': {
        'max_length': "Prezime je predugačko",
        'min_length': "Prezime je prekatko",
        'required': "Ovo polje je obavezno",
    },
    'email': {
        'invalid': "Molimo unesite validnu e-mail adresu",
        'unique': "E-mail adresa je već u upotrebi",
        'required': "Ovo polje je obavezno",
    },
    'company_position': {
        'max_length': "Ime je predugačko",
        'required': "Ovo polje je obavezno",
    },
}

LABEL_TEXT_USER = {
    'username': _('Korisničko ime'),
    'first_name': _('Ime'),
    'last_name': _('Prezime'),
    'gender': _('Pol'),
    'email': _('E-mail'),
    'company_position': _('Pozicija'),
    'work_location': _('Lokacija'),
    'is_admin': _('Administrator'),
    'is_editor': _('Moderator sajta'),
    'birth_date': _('Datum rođenja'),
    'phone': _('Telefon'),
    'business_phone': _('VPN broj'),
}

PROFILE_LABEL_TEXT = {
    'first_name': _('Ime'),
    'last_name': _('Prezime'),
    'email': _('E-mail'),
    'profile_pic': _('Avatar'),
    'birth_date': _('Datum rođenja'),
    'phone': _('Telefon'),
    'business_phone': _('VPN broj'),
}

# users/views.py
USER_CARDS_PER_PAGE = 9
