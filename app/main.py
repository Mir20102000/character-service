from fastapi import FastAPI, APIRouter

app = FastAPI(openapi_url="/api/v1/characters/openapi.json", docs_url="/api/v1/characters/docs")

characters_router = APIRouter()

characters = [
    {'books_id': 1, 'name': 'Jesus',
     'language': 'Russian',
     'age': '21', 'number_of_mentions': '650'},
    {'books_id': 2, 'name': 'Dumbledore',
     'language': 'English',
     'age': '80', 'number_of_mentions': '450'},
    {'books_id': 3, 'name': 'Batman',
     'language': 'English',
     'age': '30', 'number_of_mentions': '900'},
    {'books_id': 3, 'name': 'Superman',
     'language': 'English',
     'age': '29', 'number_of_mentions': '890'}
]


@characters_router.get("/")
async def read_characters():
    return characters


@characters_router.get("/{books_id}")
async def read_character(books_id: int):
    foots = []
    for character in characters:
        if character['books_id'] == books_id:
            foots.append(character)
    return foots


app.include_router(characters_router, prefix='/api/v1/characters', tags=['characters'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
