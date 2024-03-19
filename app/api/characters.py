from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import CharacterOut, CharacterIn, CharacterUpdate
from app.api import db_manager
from app.api.service import is_book_present

characters = APIRouter()

@characters.post('/', response_model=CharacterOut, status_code=201) #localhost:8001/api/v1/characters
async def create_character(payload: CharacterIn):
    for book_id in payload.books_id:
        if not is_book_present(book_id):
            raise HTTPException(status_code=404, detail=f"Book with given id:{book_id} not found")

    character_id = await db_manager.add_character(payload)
    response = {
        'id': character_id,
        **payload.dict()
    }

    return response

@characters.get('/', response_model=List[CharacterOut]) #localhost:8001/api/v1/characters
async def get_characters():
    return await db_manager.get_all_characters()

@characters.get('/{id}/', response_model=CharacterOut) #localhost:8001/api/v1/characters/1
async def get_character(id: int):
    character = await db_manager.get_character(id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@characters.put('/{id}/', response_model=CharacterOut) #localhost:8001/api/v1/characters/1 - Обновит страницу
async def update_character(id: int, payload: CharacterUpdate):
    character = await db_manager.get_character(id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    update_data = payload.dict(exclude_unset=True)

    if 'books_id' in update_data:
        for book_id in payload.books_id:
            if not is_book_present(book_id):
                raise HTTPException(status_code=404, detail=f"Book with given id:{book_id} not found")

    character_in_db = CharacterIn(**character)

    updated_character = character_in_db.copy(update=update_data)

    return await db_manager.update_character(id, updated_character)

@characters.delete('/{id}/', response_model=None) #localhost:8001/api/v1/characters/1 - Удалит страницу
async def delete_character(id: int):
    character = await db_manager.get_character(id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return await db_manager.delete_character(id)