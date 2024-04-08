from db.models.likes import Likes
from backend.utils.repository import LikesORMRepository


class LikesRepository(LikesORMRepository):
    model = Likes # Set the model attribute of LikesRepository to the Likes model
