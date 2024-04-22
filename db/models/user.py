from tortoise import fields  # Importing fields from Tortoise for defining model fields
from tortoise.models import Model  # Importing Model from Tortoise for defining ORM models


# Defining a Tortoise ORM model for User
class User(Model):
    id = fields.IntField(pk=True)  # Primary key field for the user's ID
    telegram_id = fields.IntField(unique=True)  # Unique field for the user's Telegram ID
    name = fields.CharField(max_length=100)  # Field for the user's name, limited to 100 characters
    username = fields.CharField(max_length=235,
                                null=True)  # Field for the user's username, nullable and limited to 235 characters
    age = fields.IntField()  # Field for the user's age
    gender = fields.CharField(max_length=100)  # Field for the user's gender, limited to 100 characters
    looking_for = fields.CharField(max_length=100)  # Field for what the user is looking for, limited to 100 characters
    city = fields.CharField(max_length=100)  # Field for the user's city, limited to 100 characters
    about = fields.TextField(max_length=225,
                             null=True)  # Field for a short description about the user limited to 225 characters
    photo = fields.CharField(max_length=225)  # Field for the user's photo URL or identifier, limited to 225 characters

    def __str__(self) -> str:
        return self.name  # String representation of the User model, returns the user's name
