from typing import List, Optional, Union
from pydantic import UUID1, BaseModel, Field
from datetime import date, time


class EventSummary(BaseModel):
    base_event_id: Optional[Union[UUID1, str]] = Field(
        description="Identifier for the plan (UUID)",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6",
    )
    # we add a field to save the event date, which is necessary to check
    # if the saved event has the most recent date.
    date_query: Optional[str] = Field(description="This is the date of the event.")
    title: Optional[str] = Field(description="Title of the plan")

    # We change the original descriptions of the date fields to clarify
    # that actually these are the selling dates.
    start_date: Optional[date] = Field(
        description="Date when the event starts the sell in local time", example="2021-02-01"
    )
    start_time: Optional[time] = Field(
        description="Time when the event starts the sell in local time", example="14:45:15"
    )
    end_date: Optional[date] = Field(
        description="Date when the event ends the sell in local time", example="2022-02-02"
    )
    end_time: Optional[time] = Field(
        description="Time when the event ends the sell in local time", example="22:38:19"
    )
    min_price: Optional[float] = Field(
        description="Min price from all the available tickets"
    )
    max_price: Optional[float] = Field(
        description="Max price from all the available tickets"
    )

EventList = List[EventSummary]
