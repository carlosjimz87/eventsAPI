from datetime import datetime
from typing import List, Optional

import requests
from requests import Response
from requests.exceptions import MissingSchema

from models.events import EventList
from providers.fake_responses import FakeResponses
from utils.xml_parser import XMLParser


class FakeProvider:

    @staticmethod
    def get_events_on_dates(query_dates: List[datetime]):
        events: EventList = []
        for date in query_dates:
            event = FakeProvider.get_events_on_date(date)
            if event is not None:
                events.extend(event)
        return events

    @staticmethod
    def get_events_on_date(date: datetime) -> Optional[EventList]:
        response = FakeProvider.request_events(date)
        if response is None or response.status_code != 200:
            return None
        return XMLParser.parse_text_on_date(response.content, date)

    @staticmethod
    def request_events(date: datetime) -> Optional[Response]:

        try:
            return requests.get(FakeResponses.events_urls(date))
        except MissingSchema:
            pass
            # print(f"NO EVENTS FOR DATE {date}.")
        # except requests.exceptions.Timeout:
        #     raise Exception(f"Server not responding")
        # except requests.exceptions.TooManyRedirects:
        #     raise Exception(f"Server not responding")
        # except requests.exceptions.RequestException:
        #     raise Exception(f"Server not responding")
