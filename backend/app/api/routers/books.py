from app.api.dependencies.core import DBSessionDep
from app.crud.book import (
    get_book_list,
    get_department_list,
    create_department,
    delete_department,
    create_book,
    create_book_copy,
    delete_book_copy,
)
from app.schemas.book import (
    BookInput,
    BookOutput,
    BookList,
    OutputDepartment,
    InputDepartment,
    BookCopyInput,
    BookCopyOutput,
)
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
import datetime


router = APIRouter(
    prefix="/api/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    response_model=BookOutput,
)
async def department_create(
    db_session: DBSessionDep,
    input_book: BookInput,
):
    book = await create_book(db_session, input_book)
    return book


@router.get(
    "/",
    response_model=List[Optional[BookList]],
)
async def book_list(
    db_session: DBSessionDep,
    author: str = None,
    year: datetime.datetime = None,
    department: str = None,
    exist: bool = None,
):
    books = await get_book_list(db_session, author, year, department, exist)
    return books


@router.get(
    "/departments/",
    response_model=List[Optional[OutputDepartment]],
)
async def department_list(
    db_session: DBSessionDep,
):
    departments = await get_department_list(db_session)
    print(departments)
    return departments


@router.post(
    "/departments/",
    response_model=Optional[OutputDepartment],
)
async def department_create(
    db_session: DBSessionDep,
    input_department: InputDepartment,
):
    department = await create_department(db_session, input_department)
    return department


@router.delete(
    "/departments/{department_id}",
)
async def department_delete(
    db_session: DBSessionDep,
    department_id: int,
):
    department = await delete_department(db_session, department_id)
    return department


@router.post(
    "/book-copy/",
    response_model=Optional[BookCopyOutput],
)
async def book_copy_create(
    db_session: DBSessionDep,
    input_book_copy: BookCopyInput,
):
    book_copy = await create_book_copy(db_session, input_book_copy)
    return book_copy


@router.delete(
    "/book-copy/",
)
async def book_copy_delete(db_session: DBSessionDep, book_id: int, user_id: int):
    book_copy = await delete_book_copy(db_session, book_id, user_id)
    return book_copy
