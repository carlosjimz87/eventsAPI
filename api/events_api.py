import asyncio
import concurrent.futures
from datetime import datetime
from typing import List, Union

import nest_asyncio

from models.events import EventList
from providers.fake_provider import FakeProvider
from utils.validator import Validator


class EventsApi:
    def __init__(self, use_workers: bool, max_workers: int) -> None:
        self.max_workers = max_workers
        self.use_workers = use_workers

    def get_available_events(
        self, starts_at: Union[str, datetime], ends_at: Union[str, datetime]
    ) -> EventList:
        starts_at = Validator.is_valid_date(starts_at)
        ends_at = Validator.is_valid_date(ends_at)

        # getting all days to make the search
        query_dates = Validator.range_of_dates(starts_at, ends_at)

        if self.use_workers:
            nest_asyncio.apply()
            # retrieve filtered events of most recent dates - asynchronously
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            events = loop.run_until_complete(self.async_request(query_dates))
        else:
            # retrieve filtered events of most recent dates - synchronously
            events = FakeProvider.get_events_on_dates(query_dates)

        return FakeProvider.get_unique_most_recent_events(events)

    async def async_request(self, dates_to_query: List[datetime]) -> EventList:
        events = []
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(
                    executor, FakeProvider.get_events_on_date, dates_to_query[i]
                )
                for i in range(0, len(dates_to_query))
            ]
            for events_on_date in await asyncio.gather(*futures):
                events.extend(events_on_date)

        return events
