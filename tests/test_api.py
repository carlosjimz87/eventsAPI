from unittest import TestCase

from api.events_api import EventsApi
from tests.test_data import TestData


class TestAPI(TestCase):

    def test_get_available_events(self):
        events = EventsApi().get_available_events(TestData.STARTS_AT, TestData.ENDS_AT)

        self.assertNotEqual(events, None)
        self.assertEqual(3, len(events))

        self.assertEqual("291", events[0].base_event_id)
        self.assertEqual("1591", events[1].base_event_id)
        self.assertEqual("322", events[2].base_event_id)
