from fastapi.params import Query
from datetime import datetime

from starlette.responses import RedirectResponse

from models.queries import StartsSearchQuery, EndsSearchQuery
from typing import Optional
from fastapi import APIRouter
from api.events_api import EventsApi
from models.responses import BaseResponse
from models.errors import GenericError, MissingDateParameter
router = APIRouter()


@router.get(
    "/search",
    summary="Lists the available events on a time range",
    response_model=BaseResponse,
    responses={400: {"model": GenericError}, 500: {"model": GenericError}},
)
async def search(starts_at: Optional[datetime] = StartsSearchQuery,
                 ends_at: Optional[datetime] = EndsSearchQuery
                 ):

    data = EventsApi().get_available_events(starts_at, ends_at)
    return BaseResponse(data=data, error=None)


@router.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')

