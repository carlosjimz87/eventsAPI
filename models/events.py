from typing import List, Optional, Union
from pydantic import UUID1, BaseModel, Field
from datetime import date, time


class EventSummary(BaseModel):
    base_event_id: Optional[Union[UUID1, str]] = Field(
        description="Identifier for the plan (UUID)",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6",
    )
    title: Optional[str] = Field(description="Title of the plan")
    start_date: Optional[date] = Field(
        description="Date when the event starts in local time", example="2021-02-01"
    )
    start_time: Optional[time] = Field(
        description="Time when the event starts in local time", example="14:45:15"
    )
    end_date: Optional[date] = Field(
        description="Date when the event ends in local time", example="2022-02-02"
    )
    end_time: Optional[time] = Field(
        description="Time when the event ends in local time", example="22:38:19"
    )
    min_price: Optional[float] = Field(
        description="Min price from all the available tickets"
    )
    max_price: Optional[float] = Field(
        description="Max price from all the available tickets"
    )


EventList = List[EventSummary]
