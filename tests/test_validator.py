from unittest import TestCase
from datetime import datetime, timezone, timedelta

from models.events import EventSummary
from utils.validator import Validator
from utils.xml_parser import XMLParser


class TestValidator(TestCase):

    def test_is_online(self):
        event = {
            "base_event_id": "291",
            "sell_mode": "online",
            "title": "Camela en concierto",
            "start_date": "2020-07-01",
            "start_time": "00:00:00",
            "end_date": "2021-06-30",
            "end_time": "20:00:00",
            "max_price": "30.00",
            "min_price": "15.00",
        }

        is_online = Validator.is_online(event)
        self.assertEqual(is_online, True)

    def test_is_valid_datetime(self):
        date = datetime(year=2021, month=1, day=1, hour=10, minute=00, second=10, tzinfo=timezone.utc)
        response_date = Validator.is_valid_date(date)
        delta = date - response_date
        self.assertEqual(delta, timedelta(0))

    def test_is_valid_date_str(self):
        pass
        # dateStr = "2021-02-08T00:00:00Z"
        # response_date = Validator.is_valid_date(dateStr)
        # dateConv = response_date.strftime("%Y-%m-%dT%H:%M:%S%z")
        # self.assertEqual(dateStr, dateConv)
