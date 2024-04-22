from tortoise import fields  # Importing fields from Tortoise for defining model fields
from tortoise.models import Model  # Importing Model from Tortoise for defining ORM models


# Defining a Tortoise ORM model for Likes
class Likes(Model):
    id = fields.IntField(pk=True)  # Primary key field for the like ID
    from_user_id = fields.IntField()  # Field for the ID of the user giving the like
    to_user_id = fields.IntField()  # Field for the ID of the user receiving the like
    time = fields.DatetimeField(auto_now_add=True)  # Field for the timestamp of when the like was given

    def __str__(self):
        return f"{self.from_user_id} likes {self.to_user_id}"  # String representation of a like instance
