from calendar import HTMLCalendar
from datetime import datetime

from django.db.models import Q
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def format_day(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        for event in events_per_day:
            if event.type == 'Rođendan':
                d += f"<a onclick='displayModal(EVENT_PREVIEW_URL+{event.id})'><li> {event.title} " \
                     f"<i class='fa-solid fa-cake-candles'></i> </li></a>"
            else:
                d += f"<a onclick='displayModal(EVENT_PREVIEW_URL+{event.id})'><li>{event.title} {event.start_time.strftime('%H:%M')}</li></a>"

        if day != 0:
            return f"<td><span class='date'><a onclick='displayModal(CALENDAR_EVENTS_URL+\"{self.year}/{self.month}/{day}\")'>{day}<a/>" \
                   f"</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def format_week(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.format_day(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def format_month(self, user):
        events = Event.objects.filter(Q(author=user) | Q(shared=user),
                                      Q(start_time__year=self.year) | Q(type='Rođendan'),
                                      start_time__month=self.month).distinct()

        cal = '<table class="calendar">\n'
        # cal += f'{self.formatmonthname(self.year, self.month, )}\n'
        cal += '<th class="mon">Pon</th><th class="tue">Uto</th><th class="wed">Sri</th><th class="thu">' \
               'Čet</th><th class="fri">Pet</th><th class="sat">Sub</th><th class="sun">Ned</th>\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.format_week(week, events)}\n'
        cal += '</table>\n'
        return cal


def str_2_date(date, time):
    created_date = datetime.strptime(date, '%Y-%m-%d').date()
    created_time = datetime.strptime(time, '%H:%M').time()
    return datetime.combine(created_date, created_time)
