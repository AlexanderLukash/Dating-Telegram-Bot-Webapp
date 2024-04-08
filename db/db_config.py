from tortoise import Tortoise


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url='mysql://lukash:sasha2627@127.0.0.1:3306/dating_database',
        modules={'models': ['db.models.user', 'db.models.likes']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
