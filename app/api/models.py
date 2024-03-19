from pydantic import BaseModel
from typing import List, Optional


class CharacterIn(BaseModel):
    name: str
    description: str
    age: int
    number_of_mentions: int
    books_id: int


class CharacterOut(CharacterIn):
    id: int


class CharacterUpdate(CharacterIn):
    name: Optional[str] = None
    description: Optional[str] = None
    age: Optional[int] = None
    number_of_mentions: Optional[int] = None
    books_id: Optional[int] = None
