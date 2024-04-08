from backend.repositories.likes import LikesRepository
from backend.repositories.users import UsersRepository
from backend.services.likes import LikesService
from backend.services.users import UsersService


# Define a function to return an instance of LikesService
def likes_service():
    return LikesService(LikesRepository)  # Return a new instance of LikesService initialized with LikesRepository


# Define a function to return an instance of UsersService
def users_service():
    return UsersService(UsersRepository)  # Return a new instance of UsersService initialized with UsersRepository
