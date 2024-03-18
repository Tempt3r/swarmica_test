from app.api.dependencies.core import DBSessionDep
from app.crud.user import get_user, get_user_by_username, create_user, delete_user, get_user_list
from app.schemas.user import IntputUser, OutputUser, UserList, UserDetail
from fastapi import APIRouter, HTTPException
from typing import List, Optional


router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/{user_id}",
    response_model=UserDetail,
)
async def user_details(
    user_id: int,
    db_session: DBSessionDep,
):
    user = await get_user(db_session, user_id)
    return user


@router.post("/", response_model=OutputUser)
async def create_user_api(input_user: IntputUser, db: DBSessionDep):
    user_db = await get_user_by_username(db, username=input_user.username)
    if user_db:
        raise HTTPException(status_code=400, detail="User already registered")
    user = await create_user(db=db, user=input_user)
    return user


@router.get(
    "/",
    response_model=List[Optional[UserList]],
)
async def users_list(
    db_session: DBSessionDep,
):
    users = await get_user_list(db_session)
    return users


@router.delete(
    "/{user_id}",
)
async def user_details(
    user_id: int,
    db_session: DBSessionDep,
):
    user = await delete_user(db_session, user_id)
    return user