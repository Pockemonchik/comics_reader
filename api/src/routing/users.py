from typing import Annotated
from fastapi import APIRouter, Depends, status,HTTPException


from schemas.user_schema import (
    UserSchemaCreate,
    UserSchema,
    UserSchemaUpdate,
    UserSchemaUpdatePartial,
)
from routing.dependencies import user_service
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserSchema])
async def get_users(
    users_service: Annotated[UserService, Depends(user_service)],
):
    users = await users_service.get_users()
    return users


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user: UserSchemaCreate,
    user_service: Annotated[UserService, Depends(user_service)],
):
    user_id = await user_service.add_user(user)
    return {"user_id": user_id}


@router.get("/{user_id}/")
async def get_user(
    user_id: int, user_service: Annotated[UserService, Depends(user_service)]
):
    user = await user_service.get_user(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@router.patch("/{user_id}/")
async def update_user_partial(
    user_id: int,
    user_update: UserSchemaUpdatePartial,
    user_service: Annotated[UserService, Depends(user_service)],
):
    user_id = await user_service.update_user(id=user_id, user=user_update)
    if not user_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"user_id": user_id}


@router.put("/{user_id}/")
async def update_user(
    user_id: int,
    user_update: UserSchemaUpdate,
    user_service: Annotated[UserService, Depends(user_service)],
):
    user_id = await user_service.update_user(id=user_id, user=user_update)
    if not user_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"user_id": user_id}


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    user_service: Annotated[UserService, Depends(user_service)],
) -> None:
    user_id = await user_service.delete_user(id=user_id)
    if not user_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"user_id": user_id}
