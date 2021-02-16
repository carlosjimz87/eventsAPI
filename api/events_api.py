from models.errors import MissingDateParameter, GenericError
from models.events import EventSummary, EventList
from utils.formatter import Formatter
from providers.fake_provider import FakeProvider
from typing import Dict, Union, List, Type, Optional
from requests.exceptions import MissingSchema

from utils.validator import Validator
from utils.xml_parser import XMLParser
from datetime import datetime, timedelta


class EventsApi:
    @staticmethod
    def get_available_events(
            starts_at: Union[str, datetime],
            ends_at: Union[str, datetime]) -> EventList:

        starts_at = Validator.is_valid_date(starts_at)
        ends_at = Validator.is_valid_date(ends_at)

        # getting all days to make the search
        query_dates = EventsApi.get_query_dates(ends_at, starts_at)
        events: EventList = []

        # retrieve events for each day
        for date in query_dates:
            events.extend(EventsApi.get_events_on_date(date))

        return events

    @staticmethod
    def get_events_on_date(date: datetime) -> EventList:
        events: EventList = []
        dateStr = Formatter.date_to_str(date)

        response = FakeProvider.events_on_date(dateStr)
        if response is not None and response.status_code == 200:
            tree = XMLParser.parse_str(response.content)
            XMLParser.parse_base_event(events, tree)

        return events

    @staticmethod
    def get_query_dates(ends_at: datetime, starts_at: datetime):
        delta = EventsApi.get_delta(ends_at, starts_at)
        return [(ends_at - timedelta(days=i)) for i in range(delta.days + 1)]

    @staticmethod
    def get_delta(ends_at: datetime, starts_at: datetime) -> timedelta:
        return abs(ends_at - starts_at)
