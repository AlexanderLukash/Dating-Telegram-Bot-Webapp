from abc import ABC, abstractmethod
from tortoise import Model


# Define an abstract base class for repositories
class AbstractRepository(ABC):
    @abstractmethod
    async def find_all(self):  # Abstract method to find all records
        raise NotImplementedError


# Concrete repository implementing the abstract class
class TortoiseORMRepository(AbstractRepository):
    model = None  # Placeholder for the model

    async def find_all(self):  # Implementation of find_all method
        res = await self.model.all()
        return res


# Repository for handling User model operations
class UsersORMRepository(TortoiseORMRepository):
    # Method to get one user by ID
    async def get_one(self, data: int):
        res = await self.model.filter(telegram_id=data).first()
        return res

    # Method to find users by city
    async def find_by_city(self, data: str):
        res = await self.model.filter(city=data)
        return res

    # Method to find users by age
    async def find_by_age(self, data: int):
        res = await self.model.filter(age=data)
        return res

    # Method to find users based on criteria
    async def find_best_result(self, data: dict):
        res = await self.model.filter(
            city=data.get("city"),
            age__gte=data.get("age__gte"),
            age__lte=data.get("age__lte"),
            gender=data.get("gender")
        ).exclude(telegram_id=data.get("telegram_id"))
        return res

    # Method to update users photo
    async def photo_update(self, data: dict):
        res = await self.model.filter(telegram_id=data.get('telegram_id')).first()

        res.photo = data.get('photo_url')
        await res.save()
        return res

    # Method to update users about info
    async def about_update(self, data: dict):
        res = await self.model.filter(telegram_id=data.get('telegram_id')).first()

        res.about = data.get('about')
        await res.save()
        return res

    # Method to update or create new users
    async def create_update_user(self, data: dict):
        res = await self.model.update_or_create(
            telegram_id=data.get('telegram_id'),
            defaults={
                'username': data.get('username'),
                'name': data.get('name'),
                'age': data.get('age'),
                'gender': data.get('gender'),
                'looking_for': data.get('looking_for'),
                'city': data.get('city'),
                'about': data.get('about'),
                'photo': data.get('photo')
            })
        return res


# Repository for handling Likes model operations
class LikesORMRepository(TortoiseORMRepository):
    # Method to create a like
    async def create_like(self, from_user: int, to_user: int):
        res = await self.model.create(
            from_user_id=from_user,
            to_user_id=to_user
        )
        return res

    # Method to get a specific like
    async def get_like(self, from_user: int, to_user: int):
        res = await self.model.filter(from_user_id=from_user, to_user_id=to_user).first()
        return res

    # Method to find likes from a user
    async def find_likes_from_user(self, data: int) -> Model:
        res = await self.model.filter(from_user_id=data)
        return res

    # Method to find likes to a user
    async def find_likes_to_user(self, data: int) -> Model:
        res = await self.model.filter(to_user_id=data)
        return res

    # Method to delete a like
    async def delete_like(self, from_user: int, to_user: int):
        res = await self.get_like(from_user, to_user)
        await res.delete()
        return res
