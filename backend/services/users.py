from backend.utils.repository import UsersORMRepository


class UsersService:
    # Initialize the UsersService with a UsersORMRepository instance
    def __init__(self, users_repo: UsersORMRepository):
        self.users_repo: UsersORMRepository = users_repo()

    async def get_user(self, data: int):
        user = await self.users_repo.get_one(data)  # Get a user by ID using the repository
        return user

    async def get_users(self):
        users = await self.users_repo.find_all()  # Get all users using the repository
        return users

    async def get_users_by_city(self, data: str):
        users = await self.users_repo.find_by_city(data)  # Get users by city using the repository
        return users

    async def get_users_by_age(self, data: int):
        users = await self.users_repo.find_by_age(data)  # Get users by age using the repository
        return users

    async def get_best_result(self, data: int):
        user = await self.users_repo.get_one(data)
        min_age = user.age - 3
        max_age = user.age + 3
        data = {"city": user.city, "gender": user.looking_for, "age__gte": min_age, "age__lte": max_age}
        users = await self.users_repo.find_best_result(data)  # Find best matching users using the repository
        return users
