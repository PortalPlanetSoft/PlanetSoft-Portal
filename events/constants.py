from django.utils.translation import gettext_lazy as _

# utils.py
EVENTS_URL_ADDRESS = 'http://127.0.0.1:8000/calendar/events/'

# calendar.html
MONTHS = ['Januar', 'Februar', 'Mart', 'April', 'Maj maj maj sto mi dodje ovaj dan', 'Juni', 'Juli', 'Avgust',
          'Septembar', 'Oktobar', 'Novembar', 'Decembar']


JANUARY = 1
DECEMBER = 12

PREVIOUS = 1
NEXT = 1

# forms.py
LABEL_TEXT_EVENT = {
    'title': _('Naslov'),
    'details': _('Detalji'),
    'shared': _('Dodijeljeni korisnici'),
    'start_time': _('Datum i vrijeme početka događaja'),
    'end_time': _('Datum i vrijeme kraja događaja'),
    'repeat_days': _('Ponoviće se za dana'),
    'repeat_every_year': _('Ponavlja se svake godine?'),
    'type': _('Tip događaja'),
}

EVENT_TYPES = [
    ('Birthday', 'Rođendan'),
    ('Meeting', 'Sastanak'),
    ('Daily', 'Daily'),
    ('Planning', 'Planiranje'),
]
