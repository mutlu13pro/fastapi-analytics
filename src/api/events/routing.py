from fastapi import APIRouter
from .schemas import EventListSchema, EventSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()


# GET /api/events
@router.get("/")
def read_events() -> EventListSchema:
    # list of the events
    return {"results": [{"id": 1}, {"id": 2}, {"id": 3}], "count": 3}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # get the event by id
    return {"id": event_id}


# ~ SEND  DATA HERE
# create view
# POST /api/events
@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    print(payload.page)
    return {"id": 123}


# ~ UPDATE DATA HERE
# create view
# PUT /api/events
@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    print(payload.description)
    return {"id": event_id}
