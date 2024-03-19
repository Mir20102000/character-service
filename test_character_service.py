import requests


def test_get_all_characters(url: str):
    res = requests.get(url).json()
    assert (res == [
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
    ])


def test_get_character_by_id(url: str):
    res = requests.get(url).json()
    assert (res == [{'books_id': 3, 'name': 'Akinfeev',
                     'language': 'Russia',
                     'age': '90', 'number_of_mentions': '47'},
                    {'books_id': 3, 'name': 'Dzagoev',
                     'language': 'Russia',
                     'age': '105', 'number_of_mentions': '36'}])


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/characters/'
    test_get_character_by_id(URL + '3')
    test_get_all_characters(URL)
