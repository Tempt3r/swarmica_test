from pydantic import BaseModel, ConfigDict, computed_field
from app.schemas.book import BookToUser
from asyncio import run
from typing import Optional, List


class IntputUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str


class OutputUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str


class UserList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int]
    username: Optional[str]
    books_count: Optional[int]


class UserDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int]
    username: Optional[str]
    books: Optional[List[Optional[BookToUser]]]
