from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, String, DateTime, Integer, CheckConstraint
from typing import Optional, List
import datetime
from .user import User
from . import Base


class Department(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(index=True, unique=True)


class Book(Base):
    __tablename__ = "book"
    __table_args__ = {"extend_existing": True}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(index=True, unique=True)
    author: Mapped[Optional[str]] = mapped_column(String(256))
    year: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    copies_number: Mapped[int]
    department_id = mapped_column(Integer, ForeignKey("department.id", ondelete="CASCADE"))
    department = relationship("Department")
    copies: Mapped[List["BookCopy"]] = relationship(back_populates="book")

    # __table_args__ = (
    #     CheckConstraint(copies_number >= 0, name='check_copies_number_positive'),
    #     {})


class BookCopy(Base):
    __tablename__ = "book_copy"
    __table_args__ = {"extend_existing": True}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    book_id = mapped_column(Integer, ForeignKey("book.id", ondelete="CASCADE"))
    book: Mapped[Book] = relationship(Book, back_populates="copies")
    user: Mapped[User] = relationship(User, back_populates="books")
    user_id = mapped_column(Integer, ForeignKey(User.id, ondelete="CASCADE"))
