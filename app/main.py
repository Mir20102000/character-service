from fastapi import FastAPI, APIRouter

app = FastAPI(openapi_url="/api/v1/characters/openapi.json", docs_url="/api/v1/characters/docs")

characters_router = APIRouter()

characters = [
    {'books_id': 1, 'name': 'Mbappe',
     'language': 'France',
     'age': '50', 'number_of_mentions': '34'},
    {'books_id': 2, 'name': 'Ronaldo',
     'language': 'Portugal',
     'age': '5', 'number_of_mentions': '26'},
    {'books_id': 3, 'name': 'Akinfeev',
     'language': 'Russia',
     'age': '90', 'number_of_mentions': '47'},
    {'books_id': 3, 'name': 'Dzagoev',
     'language': 'Russia',
     'age': '105', 'number_of_mentions': '36'}
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
