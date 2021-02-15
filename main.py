from fastapi import FastAPI

from api.events_api import EventsApi

app = FastAPI(
    title="Events API Fever",
    description="This is a Python based API to retrieve events information from an external provider.",
    version="1.0.0"
)


@app.get("/search")
async def get_events():
    response = EventsApi().get_available_events("2021-02-09")
    return response
