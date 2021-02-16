from typing import Literal, Optional

from pydantic import BaseModel, Field

from models.events import EventList


class BaseResponse(BaseModel):

    data: Optional[EventList]
    error: Literal[None] = Field(None)
