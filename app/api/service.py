import os
import httpx

BOOK_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/books/'


def is_book_present(book_id: int):
    return True
