import environ
from tortoise import Tortoise

env = environ.Env()
environ.Env.read_env('.env')

db_url = (f'postgres://{env('POSTGRES_USER')}:{env('POSTGRES_PASSWORD')}@{env('POSTGRES_HOST')}:'
          f'{env('POSTGRES_PORT')}/{env('POSTGRES_DB')}')

print(db_url)


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ['db.models.user', 'db.models.likes']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
