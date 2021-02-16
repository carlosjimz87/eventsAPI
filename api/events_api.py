from datetime import datetime
from typing import Union, Dict

from models.events import EventList, EventSummary
from providers.fake_provider import FakeProvider
from utils.validator import Validator


class EventsApi:

    @staticmethod
    def get_available_events(starts_at: Union[str, datetime], ends_at: Union[str, datetime]) -> EventList:

        starts_at = Validator.is_valid_date(starts_at)
        ends_at = Validator.is_valid_date(ends_at)

        # getting all days to make the search
        query_dates = Validator.range_of_dates(starts_at, ends_at)

        # retrieve events filter to the most recent dates
        return FakeProvider.get_events_on_dates(query_dates)

