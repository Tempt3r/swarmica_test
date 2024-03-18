from pydantic import BaseModel, ConfigDict
import datetime
from typing import Optional


class OutputDepartment(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int]
    title: Optional[str]


class InputDepartment(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str


class BookList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int]
    title: Optional[str]
    author: Optional[str]
    year: Optional[datetime.datetime]
    copies_number: Optional[int]
    department_id: Optional[int]


class BookInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    author: str
    year: datetime.datetime
    copies_number: int
    department_id: int


class BookOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    author: str
    year: datetime.datetime
    copies_number: int
    department_id: int


class BookCopyInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    book_id: int
    user_id: int


class BookCopyOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    book_id: int
    user_id: int


class BookToUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    book: BookOutput
