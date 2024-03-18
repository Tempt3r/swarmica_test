from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import aggregated
from sqlalchemy import Column, Integer, func
from typing import List
from . import Base


class User(Base):
    __tablename__ = "book_users"
    __table_args__ = {"extend_existing": True}
    # __table_args__ = {'quote': False}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[str]
    books: Mapped[List["BookCopy"]] = relationship(back_populates="user")

    @aggregated('books', Column(Integer))
    def books_count(self):
        return func.count('1')