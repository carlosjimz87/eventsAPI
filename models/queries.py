from fastapi.params import Query


StartsSearchQuery = Query(
    None,
    description="Return only events that starts after this date",
    example="2021-02-08T00:00:00Z",
)


EndsSearchQuery = Query(
    None,
    description="Return only events that finishes before this date",
    example="2021-02-12T00:00:00Z",
)
