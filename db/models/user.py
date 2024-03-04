from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class User(models.Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.IntField(unique=True)
    name = fields.CharField(max_length=100)
    username = fields.CharField(max_length=235)
    age = fields.IntField(min_value=13)
    gender = fields.IntField(min_value=1, max_value=2)
    city = fields.CharField(max_length=100)
    about = fields.TextField(max_length=225)
    photo = fields.CharField(max_length=225)


    def __str__(self):
        return self.name

    class PydanticMeta:
        exclude = ["telegram_id"]


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
