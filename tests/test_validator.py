from unittest import TestCase
from datetime import datetime, timezone, timedelta

from models.events import EventSummary
from tests.test_data import TestData
from utils.validator import Validator


class TestValidator(TestCase):

    def test_is_online(self):

        is_online = Validator.is_online(TestData.Event)
        self.assertEqual(is_online, True)

    def test_is_valid_datetime(self):
        response_date = Validator.is_valid_date(TestData.EVENT_DATE)
        delta = TestData.EVENT_DATE - response_date
        self.assertEqual(delta, timedelta(0))

    def test_range_of_dates_with_dates(self):
        days = Validator.range_of_dates(TestData.STARTS_AT, TestData.ENDS_AT)
        self.assertEqual(len(days), 367)

    def test_range_of_dates_without_dates(self):
        days = Validator.range_of_dates(TestData.STARTS_AT)
        self.assertEqual(len(days), 10)

    def test_range_of_dates_without_days(self):
        days = Validator.range_of_dates(TestData.STARTS_AT, days=7)
        self.assertEqual(len(days), 7)

    def test_delta(self):
        delta = Validator.delta(TestData.STARTS_AT, TestData.ENDS_AT)
        self.assertEqual(delta, timedelta(366))
