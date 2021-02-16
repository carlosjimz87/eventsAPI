from unittest import TestCase

from tests.test_data import TestData
from utils.formatter import Formatter


class TestFormatter(TestCase):

    def test_str_to_date(self):
        formatted = Formatter.str_to_date(TestData.STARTS_AT.strftime("%Y-%m-%dT%H:%M:%S%z"))
        self.assertEqual(formatted, TestData.STARTS_AT)


