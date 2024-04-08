from db.models.user import User
from backend.utils.repository import UsersORMRepository


class UsersRepository(UsersORMRepository):
    model = User  # Set the model attribute of UsersRepository to the User model
