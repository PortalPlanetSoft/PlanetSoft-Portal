from calendar import HTMLCalendar

from .constants import EVENTS_URL_ADDRESS
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
            d += f'<li> {event.title} </li>'

        if day != 0:
            return f"<td><span class='date'><a href='{EVENTS_URL_ADDRESS}{self.year}/{self.month}/{day}'>{day}<a/>" \
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
    def format_month(self):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = '<table class="calendar">\n'
        # cal += f'{self.formatmonthname(self.year, self.month, )}\n'
        cal += '<th class="mon">Pon</th><th class="tue">Uto</th><th class="wed">Sri</th><th class="thu">' \
               'Čet</th><th class="fri">Pet</th><th class="sat">Sub</th><th class="sun">Ned</th>\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.format_week(week, events)}\n'
        cal += '</table>\n'
        return cal
