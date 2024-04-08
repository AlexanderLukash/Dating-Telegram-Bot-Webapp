from typing import Annotated
from fastapi import APIRouter, Depends

from backend.api.dependencies import likes_service
from backend.services.likes import LikesService

router = APIRouter(
    prefix="/likes",  # Set the router's prefix to "/likes"
    tags=["Likes"],  # Assign the router to the "Likes" tag
)


# Define endpoints for likes

@router.get("")
async def get_likes(like_service: Annotated[LikesService, Depends(likes_service)]):
    # Endpoint to get all likes
    likes = await like_service.get_likes()

    if not likes:
        return {"status": True, "data": "Likes not found!"}
    return {"status": True, "data": likes}


@router.get("/get/{from_user}/{to_user}")
async def get_like(from_user: int, to_user: int, like_service: Annotated[LikesService, Depends(likes_service)]):
    # Endpoint to check if a like exists between two users
    likes = await like_service.get_like(from_user, to_user)

    if likes:
        return {"status": True, "data": True}  # If like exists, return True
    else:
        return {"status": True, "data": False}  # If like does not exist, return False


@router.get("/get/from/{user_id}")
async def get_likes_from_user(user_id: int, like_service: Annotated[LikesService, Depends(likes_service)]):
    # Endpoint to get likes sent by a user
    users = await like_service.get_likes_from_user(user_id)

    if not users:
        return {"status": True, "data": "Likes not found!"}
    return {"status": True, "data": users}


@router.get("/get/to/{user_id}")
async def get_likes_to_user(user_id: int, like_service: Annotated[LikesService, Depends(likes_service)]):
    # Endpoint to get likes received by a user
    users = await like_service.get_likes_to_user(user_id)

    if not users:
        return {"status": True, "data": "Likes not found!"}
    return {"status": True, "data": users}


@router.post("/add/{from_user}/{to_user}")
async def add_like(from_user: int, to_user: int, like_service: Annotated[LikesService, Depends(likes_service)]):
    # Endpoint to add a like between two users
    like = await like_service.add_like(from_user, to_user)

    if not like:
        return {"status": True, "data": "The like already exists."}
    else:
        return {"status": True, "data": "Like added successfully."}


@router.delete("/remove/{from_user}/{to_user}")
async def remove_like(from_user: int, to_user: int, like_service: Annotated[LikesService, Depends(likes_service)]):
    # Endpoint to remove a like between two users
    like = await like_service.remove_like(from_user, to_user)

    if like:
        return {"status": True, "data": "Like removed successfully."}
    else:
        return {"status": True, "data": "The like does not exist."}
