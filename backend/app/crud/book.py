from app.models import Book, Department, BookCopy
from app.schemas.book import InputDepartment, BookInput, BookCopyInput
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
import datetime
from typing import List


async def create_book(db: AsyncSession, book: BookInput) -> Book:
    db_book = Book(
        title=book.title,
        author=book.author,
        year=book.year,
        copies_number=book.copies_number,
        department_id=book.department_id,
    )
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book


async def get_book_list(
    db_session: AsyncSession,
    author: str = None,
    year: datetime.datetime = None,
    department: str = None,
    exist: bool = None,
) -> List[Book]:
    statement = select(Book).order_by(Book.id)
    if author:
        statement = statement.where(Book.author == author)
    if year:
        statement = statement.where(Book.year == year)
    if department:
        statement = statement.where(Book.department_id == int(department))
    if exist:
        statement = statement.where(Book.copies_number > 0)
    books = await db_session.scalars(statement)
    return books


async def get_department_list(db_session: AsyncSession) -> List[Department]:
    statement = select(Department).order_by(Department.id)
    departments = await db_session.scalars(statement)
    return departments


async def create_department(db: AsyncSession, department: InputDepartment) -> Department:
    db_department = Department(
        title=department.title,
    )
    db.add(db_department)
    await db.commit()
    await db.refresh(db_department)
    return db_department


async def delete_department(db: AsyncSession, department_id: int):
    statement = delete(Department).where(Department.id == department_id)
    await db.execute(statement)
    await db.commit()
    return {"ok": True}


async def create_book_copy(db: AsyncSession, book_copy: BookCopyInput) -> BookCopy:
    db_book_copy = BookCopy(book_id=book_copy.book_id, user_id=book_copy.user_id)
    db.add(db_book_copy)
    book_update = update(Book).where(Book.id == book_copy.book_id).values(copies_number=Book.copies_number - 1)
    await db.execute(book_update)
    await db.commit()
    await db.refresh(db_book_copy)
    return db_book_copy


async def delete_book_copy(db: AsyncSession, book_id: int, user_id: int):
    statement = delete(BookCopy).where(BookCopy.book_id == book_id).where(BookCopy.user_id == user_id)
    await db.execute(statement)
    book_update = update(Book).where(Book.id == book_id).values(copies_number=Book.copies_number + 1)
    await db.execute(book_update)
    await db.commit()
    return {"ok": True}


async def get_book_copy_count_by_user_id(db: AsyncSession, user_id: int) -> int:
    statement = select(BookCopy).where(BookCopy.user_id == user_id).count()
    result = await db.scalars(statement)
    return result
