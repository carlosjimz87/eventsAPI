from datetime import datetime
from typing import List, Optional, Dict

import requests
from requests import Response
from requests.exceptions import MissingSchema

from models.events import EventList, EventSummary
from providers.fake_responses import FakeResponses
from utils.xml_parser import XMLParser


class FakeProvider:
    def __init__(self, max_workers: int = 4) -> None:
        self.max_workers = max_workers

    @staticmethod
    def get_events_on_dates(query_dates: List[datetime]):
        events: EventList = []
        for date in query_dates:
            event = FakeProvider.get_events_on_date(date)
            if event is not None:
                events.extend(event)
        return FakeProvider.get_unique_most_recent_events(events)

    @staticmethod
    def get_events_on_date(date: datetime) -> EventList:
        response = FakeProvider.request_events(date)
        events = []
        if response is not None and response.status_code == 200:
            events = XMLParser.parse_text_on_date(response.content, date)
        return events

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


    @staticmethod
    def get_unique_most_recent_events(events: EventList) -> EventList:
        filtered_events: Dict[str, EventSummary] = {}
        for event in events:
            eventID = event.base_event_id
            if eventID not in filtered_events:
                filtered_events[eventID] = event
            elif event.date_query > filtered_events[eventID].date_query:
                filtered_events[eventID] = event

        return [event for event in filtered_events.values()]
