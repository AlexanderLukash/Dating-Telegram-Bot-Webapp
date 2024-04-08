from typing import Annotated

from backend.api.dependencies import users_service
from fastapi import APIRouter, Depends
from backend.services.users import UsersService

router = APIRouter(
    prefix="/users",  # Set the router's prefix to "/users"
    tags=["Users"],  # Assign the router to the "Users" tag
)


# Define endpoints for users

@router.get("")
async def get_users(user_service: Annotated[UsersService, Depends(users_service)]):
    # Endpoint to get all users
    users = await user_service.get_users()

    if not users:
        return {"status": True, "data": "Users not found!"}
    return {"status": True, "data": users}


@router.get("/id/{user_id}")
async def get_user_data(user_id: int, user_service: Annotated[UsersService, Depends(users_service)]):
    # Endpoint to get user data by ID
    user = await user_service.get_user(user_id)

    if not user:
        return {"status": True, "data": "User not found!"}
    return {"status": True, "data": user}


@router.get("/city/{user_city}")
async def get_users_by_city(user_city: str, user_service: Annotated[UsersService, Depends(users_service)]):
    # Endpoint to get users by city
    users = await user_service.get_users_by_city(user_city)

    if not users:
        return {"status": True, "data": "Users not found!"}
    return {"status": True, "data": users}


@router.get("/age/{user_age}")
async def get_users_by_age(user_age: int, user_service: Annotated[UsersService, Depends(users_service)]):
    # Endpoint to get users by age
    users = await user_service.get_users_by_age(user_age)

    if not users:
        return {"status": True, "data": "Users not found!"}
    return {"status": True, "data": users}


@router.get("/best_results/{user_id}/")
async def get_users_best_results(user_id: int, user_service: Annotated[UsersService, Depends(users_service)]):
    # Endpoint to get best results for a user based on preferences
    users = await user_service.get_best_result(user_id)

    if not users:
        return {"status": True, "data": "Users not found!"}
    return {"status": True, "data": users}
