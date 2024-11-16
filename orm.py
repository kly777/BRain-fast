import asyncio
from tortoise import Tortoise


async def init_db():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url='sqlite://db/db.sqlite3',
        modules={'card': ['card.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
