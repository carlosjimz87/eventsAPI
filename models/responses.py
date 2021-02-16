from pydantic import BaseModel, Field
from typing import Optional, Literal
from models.events import EventList


class BaseResponse(BaseModel):

    data: Optional[EventList]
    error: Literal[None] = Field(None)
