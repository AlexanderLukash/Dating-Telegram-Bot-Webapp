from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.IntField(unique=True)
    name = fields.CharField(max_length=100)
    username = fields.CharField(max_length=235)
    age = fields.IntField()
    gender = fields.CharField(max_length=100)
    city = fields.CharField(max_length=100)
    about = fields.TextField(max_length=225, null=True)
    photo = fields.CharField(max_length=225)
    liked_users = fields.ManyToManyField(
        "models.User",
        related_name="liked_by",
        through="Likes",
    )

    def __str__(self) -> str:
        return self.name


class Likes(Model):
    id = fields.IntField(pk=True)
    from_user = fields.ForeignKeyField("models.User", related_name="likes_sent")
    to_user = fields.ForeignKeyField("models.User", related_name="likes_received")

    def __str__(self):
        return f"{self.from_user.username} likes {self.to_user.username}"
