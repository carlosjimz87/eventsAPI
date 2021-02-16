from typing import Literal
from pydantic import BaseModel, Field


class BaseError(BaseModel):
    error: str = Field(None, description="error code", example="string")
    message: str = Field(None, description="error message", example="string")


class GenericError(BaseModel):
    data: Literal[None] = Field(None)
    error: BaseError

    class Config:
        keep_untouched: True
        schema_extra = {
            "examples": [
                {
                    "data": None,
                    "error": {"error": 400, "message": "message"},
                }
            ]
        }


class MissingDateParameter(Exception):
    pass


class MalformedDateParameter(Exception):
    pass
