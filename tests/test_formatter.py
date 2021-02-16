from unittest import TestCase
from utils.formatter import Formatter
from datetime import datetime, timezone


class TestFormatter(TestCase):

    def test_str_to_date(self):
        formatted = Formatter.str_to_date("2021-02-08 00:00:00+00:00")
        self.assertEqual(formatted, datetime(2021, 2, 8, 0, 0, 0, tzinfo=timezone.utc))

    def test_replace_utf_format(self):
        formatted = Formatter.replace_utf_format("2021-02-08T00:00:00Z")
        self.assertEqual(formatted, "2021-02-08T00:00:00+00:00")
