from datetime import date, datetime

from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils.safestring import mark_safe
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from events.constants import MONTHS, JANUARY, DECEMBER, PREVIOUS, NEXT
from events.forms import CreateEvent
from events.models import Event
from events.utils import Calendar
from praksaPlanetSoft.constants import HTTP_STATUS_400


class CalendarView(ListView):
    model = Event
    template_name = 'events/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar if not provided
        if ('year' and 'month' in self.kwargs) and (self.kwargs['month'] and self.kwargs['month'] > 0):
            d = date(self.kwargs['year'], self.kwargs['month'], day=1)
        else:
            d = datetime.today()

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.format_month(self.request.user)
        context['year'] = d.year
        context['next_year'] = d.year + NEXT
        context['previous_year'] = d.year - PREVIOUS
        context['month'] = d.month

        if d.month == JANUARY:
            context['next_month'] = d.month + NEXT
            context['previous_month'] = DECEMBER
        elif d.month == DECEMBER:
            context['next_month'] = JANUARY
            context['previous_month'] = d.month - PREVIOUS
        else:
            context['next_month'] = d.month + NEXT
            context['previous_month'] = d.month - PREVIOUS

        context['months'] = MONTHS
        context['selected_month'] = MONTHS[d.month - PREVIOUS]
        context['calendar'] = mark_safe(html_cal)
        return context


class EventCreate(CreateView):
    model = Event
    template_name = 'events/event.html'
    success_url = '/calendar/'
    form_class = CreateEvent

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # form.fields['shared'].queryset = User.objects.exclude(id=self.request.user.id)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = HTTP_STATUS_400
        return response


class EventUpdate(UpdateView):
    model = Event
    template_name = 'events/event-edit.html'
    success_url = '/calendar/'
    form_class = CreateEvent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateEvent(instance=context['object'])
        return context

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = HTTP_STATUS_400
        return response


class EventPreview(DetailView):
    model = Event
    template_name = 'events/event-preview.html'


class EventDelete(UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/calendar/'
    template_name = 'events/event-confirm-deletion.html'

    def test_func(self):
        if self.request.user.is_admin or self.request.user.is_superuser or self.request.user.is_editor:
            return True
        elif self.request.user.is_authenticated:
            raise PermissionDenied("You are not authorized to delete events ")


class DayDetails(ListView):
    template_name = 'events/day.html'
    model = Event

    def get_queryset(self, *args, **kwargs):
        query_set = super().get_queryset().filter(start_time__year=self.kwargs['year'],
                                                  start_time__month=self.kwargs['month'],
                                                  start_time__day=self.kwargs['day'])
        return query_set
