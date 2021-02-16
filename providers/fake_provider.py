from datetime import datetime

from requests import Response
from requests.exceptions import MissingSchema

from providers.fake_responses import FakeResponses
import requests


class FakeProvider:
    @staticmethod
    def events_on_date(date: str) -> Response:
        try:
            return requests.get(FakeResponses.events_urls(date))
        except (MissingSchema, KeyError) as err:
            print(f"Date {date} not found in provider")
