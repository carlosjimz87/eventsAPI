from datetime import datetime, timezone, timedelta
from unittest import TestCase
from api.events_api import EventsApi


class TestAPI(TestCase):
    DATE_STR = "2021-02-09"
    STARTS_AT = datetime(day=1, month=1, year=2020, hour=5, minute=20, second=19, microsecond=0, tzinfo=timezone.utc)
    ENDS_AT = STARTS_AT
    ENDS_AT.replace(day=11)

    def test_get_available_events(self):
        pass
        # EventsApi.get_available_events(self.STARTS_AT, self.ENDS_AT)

    def test_get_events(self):
        events = EventsApi.get_events_on_date(self.DATE_STR)
        self.assertEqual(len(events), 3)

    def test_get_query_dates(self):
        dates = EventsApi.get_query_dates(self.ENDS_AT, self.STARTS_AT)
        self.assertEqual(len(dates), self.ENDS_AT.day)

    def test_get_delta(self):
        delta = EventsApi.get_delta(self.ENDS_AT, self.STARTS_AT)
        self.assertEqual(delta, timedelta(self.ENDS_AT.day - 1))
