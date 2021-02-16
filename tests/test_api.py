from datetime import datetime, timezone, timedelta
from unittest import TestCase
from api.events_api import EventsApi


class TestAPI(TestCase):
    STARTS_AT = datetime(day=1, month=2, year=2021, hour=5, minute=20, second=19, microsecond=0, tzinfo=timezone.utc)
    ENDS_AT = datetime(day=2, month=2, year=2022, hour=5, minute=20, second=19, microsecond=0, tzinfo=timezone.utc)
    EVENT_DATE = datetime(day=9, month=2, year=2021, hour=5, minute=20, second=19, microsecond=0, tzinfo=timezone.utc)

    # temporary we fetch duplicated events for different dates, this will be fixed in next iteration
    def test_get_available_events(self):
        eventList = EventsApi.get_available_events(self.STARTS_AT, self.ENDS_AT)
        self.assertEqual(len(eventList), 7)
        pass

    def test_get_events_on_date(self):
        events = EventsApi.get_events_on_date(self.EVENT_DATE)
        self.assertEqual(len(events), 3)

    def test_get_query_dates(self):
        dates = EventsApi.get_query_dates(self.ENDS_AT, self.STARTS_AT)
        self.assertEqual(len(dates), 367)
        self.assertEqual(dates[len(dates) - 1], self.STARTS_AT)
        self.assertEqual(dates[0], self.ENDS_AT)

    def test_get_delta(self):
        delta = EventsApi.get_delta(self.ENDS_AT, self.STARTS_AT)
        self.assertEqual(delta, timedelta(366))
