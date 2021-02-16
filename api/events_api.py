from datetime import datetime, timedelta
from typing import Union, Set, Dict, Optional

from models.events import EventList, EventSummary
from providers.fake_provider import FakeProvider
from utils.formatter import Formatter
from utils.validator import Validator
from utils.xml_parser import XMLParser


class EventsApi:
    @staticmethod
    def get_available_events(starts_at: Union[str, datetime], ends_at: Union[str, datetime]) -> EventList:

        starts_at = Validator.is_valid_date(starts_at)
        ends_at = Validator.is_valid_date(ends_at)

        # getting all days to make the search
        query_dates = EventsApi.get_query_dates(ends_at, starts_at)

        # retrieve events for each day
        events: EventList = []
        for date in query_dates:
            events.extend(EventsApi.get_events_on_date(date))

        return EventsApi.get_unique_most_recent_events(events)

    @staticmethod
    def get_events_on_date(date: datetime) -> EventList:
        events: EventList = []
        dateStr = Formatter.date_to_str(date)

        response = FakeProvider.events_on_date(dateStr)

        if response is not None and response.status_code == 200:
            events = XMLParser.parse_response(response, dateStr)

        return events

    @staticmethod
    def get_query_dates(ends_at: datetime, starts_at: datetime):
        delta = EventsApi.get_delta(ends_at, starts_at)
        return [(ends_at - timedelta(days=i)) for i in range(delta.days + 1)]

    @staticmethod
    def get_delta(ends_at: datetime, starts_at: datetime) -> timedelta:
        return abs(ends_at - starts_at)

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
