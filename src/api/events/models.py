# from pydantic import BaseModel, Field
from sqlmodel import Field, SQLModel
from typing import List, Optional

"""
EVENT
id
page
description
"""

class EventSchema(SQLModel):
    id: int
    page: Optional[str] =""
    description: Optional[str] =""


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] =Field(default="my description")

class EventUpdateSchema(SQLModel):
    description: str


class EventListSchema(SQLModel):
    results: list[EventSchema]
