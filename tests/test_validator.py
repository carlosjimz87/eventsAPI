from unittest import TestCase
from datetime import datetime, timezone, timedelta

from utils.formatter import Formatter
from utils.validator import Validator


class TestValidator(TestCase):

    def test_is_valid_datetime(self):
        date = datetime(year=2021, month=1, day=1, hour=10, minute=00, second=10, tzinfo=timezone.utc)
        response_date = Validator.is_valid_date(date)
        delta = date-response_date
        self.assertEqual(delta, timedelta(0))

    def test_is_valid_date_str(self):
        pass
        # dateStr = "2021-02-08T00:00:00Z"
        # response_date = Validator.is_valid_date(dateStr)
        # dateConv = response_date.strftime("%Y-%m-%dT%H:%M:%S%z")
        # self.assertEqual(dateStr, dateConv)
