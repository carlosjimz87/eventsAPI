from datetime import datetime, timedelta
from typing import Union, Dict, List

from models.events import EventList, EventSummary
from providers.fake_provider import FakeProvider
from utils.validator import Validator


class EventsApi:
    @staticmethod
    def get_available_events(starts_at: Union[str, datetime], ends_at: Union[str, datetime]) -> EventList:

        starts_at = Validator.is_valid_date(starts_at)
        ends_at = Validator.is_valid_date(ends_at)

        # getting all days to make the search
        query_dates = Validator.range_of_dates(starts_at,ends_at)

        # retrieve events for each day
        events = FakeProvider.get_events_on_dates(query_dates)

        # filter events to the most recent dates
        return EventsApi.get_unique_most_recent_events(events)

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
