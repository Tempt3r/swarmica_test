# need access to this before importing models
from app.database import Base
from .books import Book, BookCopy, Department
from .user import User
