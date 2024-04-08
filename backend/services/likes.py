from backend.repositories.users import UsersRepository
from backend.utils.repository import LikesORMRepository

from bot.handlers.user_commands import send_message


class LikesService:
    # Initialize the LikesService with a LikesORMRepository instance
    def __init__(self, likes_repo: LikesORMRepository) -> None:
        self.likes_repo: LikesORMRepository = likes_repo()

    async def get_likes(self):
        likes = await self.likes_repo.find_all()  # Get all likes using the repository
        return likes

    async def get_like(self, from_user: int, to_user: int):
        like = await self.likes_repo.get_like(from_user, to_user)  # Get a like between two users
        return like

    async def get_likes_from_user(self, data: int):
        likes = await self.likes_repo.find_likes_from_user(data)  # Get likes sent by a user

        if likes:
            users = []
            for i in likes:
                user = i.to_user_id
                get_user = await UsersRepository().get_one(user)  # Get the user who received the like
                users.append(get_user)
        return users  # Return the list of users who received likes from the specified user

    async def get_likes_to_user(self, data: int):
        likes = await self.likes_repo.find_likes_to_user(data)  # Get likes received by a user

        if likes:
            users = []
            for i in likes:
                user = i.from_user_id
                get_user = await UsersRepository().get_one(user)  # Get the user who sent the like
                users.append(get_user)
        return users  # Return the list of users who sent likes to the specified user

    async def add_like(self, from_user: int, to_user: int):
        like = await self.likes_repo.get_like(from_user, to_user)  # Check if a like already exists between the users

        if like:
            return False  # If the like already exists, return False
        else:
            like = await self.likes_repo.create_like(from_user, to_user)  # Create a new like
            await send_message(to_user,
                               text="<b>You were liked 💗</b>")  # Send a message to the user who received the like
            return like  # Return the created like

    async def remove_like(self, from_user: int, to_user: int):
        like = await self.likes_repo.get_like(from_user, to_user)  # Check if the like exists

        if not like:
            return False  # If the like doesn't exist, return False
        else:
            await self.likes_repo.delete_like(from_user, to_user)  # Delete the like
            return True  # Return True indicating the like was successfully removed
