from datetime import datetime
from pydantic import BaseModel, conint


class PostCreate(BaseModel):
    id: int
    title: str
    context: str
    date: datetime
    user_id: int


class PostEdit(BaseModel):
    title: str
    context: str
    date: datetime


class PostRead(BaseModel):
    id: int
    title: str
    context: str
    date: datetime
    user_id: int