import os
from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from starlette.responses import RedirectResponse

from api.events_api import EventsApi
from models.errors import GenericError, MissingDateParameter
from models.queries import EndsSearchQuery, StartsSearchQuery
from models.responses import BaseResponse
from utils.remove_errors import remove_422

router = APIRouter()


@router.get(
    "/search",
    summary="Lists the available events on a time range",
    response_model=BaseResponse,
    responses={400: {"model": GenericError}, 500: {"model": GenericError}},
)
@remove_422
async def search(
    starts_at: Optional[datetime] = StartsSearchQuery,
    ends_at: Optional[datetime] = EndsSearchQuery,
):
    if starts_at is None or ends_at is None:
        raise MissingDateParameter

    data = EventsApi(
        use_workers=os.environ.get("USE_WORKERS", True),
        max_workers=os.environ.get("MAX_WORKERS", 4),
    ).get_available_events(starts_at, ends_at)

    return BaseResponse(data=data, error=None)


@router.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")
