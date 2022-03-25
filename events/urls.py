from django.contrib.auth.decorators import login_required
from django.urls import path

from events.views import EventCreate, EventUpdate, EventDelete, DayDetails, CalendarView

urlpatterns = [
    path('', login_required(CalendarView.as_view()), name='calendar'),
    path('<int:year>/<int:month>', login_required(CalendarView.as_view()), name='specific-month-calendar'),
    path('create/', login_required(EventCreate.as_view()), name='event-create'),
    path('<int:pk>/', login_required(EventUpdate.as_view()), name='event-edit'),
    path('delete/<int:pk>/', login_required(EventDelete.as_view()), name='event-delete'),
    path('events/<int:year>/<int:month>/<int:day>', login_required(DayDetails.as_view()), name='day-events'),
]