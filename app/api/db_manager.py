from app.api.models import CharacterIn, CharacterOut, CharacterUpdate
from app.api.db import characters, database


async def add_character(payload: CharacterIn):
    query = characters.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_characters():
    query = characters.select()
    return await database.fetch_all(query=query)


async def get_character(id):
    query = characters.select(characters.c.id == id)
    return await database.fetch_one(query=query)


async def delete_character(id: int):
    query = characters.delete().where(characters.c.id == id)
    return await database.execute(query=query)


async def update_character(id: int, payload: CharacterIn):
    query = (
        characters
        .update()
        .where(characters.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
