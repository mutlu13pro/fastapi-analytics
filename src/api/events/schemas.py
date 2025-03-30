from pydantic import BaseModel
from typing import List

"""
EVENT
id
page
description
"""


class EventCreateSchema(BaseModel):
    page: str

class EventUpdateSchema(BaseModel):
    description: str

class EventSchema(BaseModel):
    id: int

class EventListSchema(BaseModel):
    results: list[EventSchema]
