from tortoise import fields
from tortoise.models import Model


class Likes(Model):
    id = fields.IntField(pk=True)
    from_user_id = fields.IntField()
    to_user_id = fields.IntField()
    time = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user_id} likes {self.to_user_id}"
