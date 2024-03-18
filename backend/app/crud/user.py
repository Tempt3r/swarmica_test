from app.models import User as UserDBModel
from app.models import BookCopy, Book
from app.schemas.user import IntputUser
from fastapi import HTTPException
from sqlalchemy import select, delete, func, cast, Integer
from sqlalchemy.ext.asyncio import AsyncSession


async def get_user(db_session: AsyncSession, user_id: int):
    user = (await db_session.scalars(select(UserDBModel).where(UserDBModel.id == user_id).join(BookCopy).join(Book))).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_user_by_username(db: AsyncSession, username: str) -> UserDBModel:
    statement = select(UserDBModel).where(UserDBModel.username == username)
    result = await db.execute(statement)
    return result.scalars().first()


async def create_user(db: AsyncSession, user: IntputUser) -> UserDBModel:
    db_user = UserDBModel(
        username=user.username,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user_by_email(db_session: AsyncSession, email: str):
    return (await db_session.scalars(select(UserDBModel).where(UserDBModel.email == email))).first()


async def delete_user(db: AsyncSession, user_id: int):
    statement = delete(UserDBModel).where(UserDBModel.id == user_id)
    await db.execute(statement)
    await db.commit()
    return {"ok": True}


async def get_user_list(db_session: AsyncSession):
    users_list = await db_session.scalars(select(UserDBModel).order_by(UserDBModel.id))
    return users_list
