import requests


def test_get_all_characters(url: str):
    res = requests.get(url).json()
    assert (res == [
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
    ])


def test_get_character_by_id(url: str):
    res = requests.get(url).json()
    assert (res == [{'books_id': 3, 'name': 'Batman',
                    'language': 'English',
                    'age': '30', 'number_of_mentions': '900'},
                    {'books_id': 3, 'name': 'Superman',
                    'language': 'English',
                    'age': '29', 'number_of_mentions': '890'}])


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/characters/'
    test_get_character_by_id(URL + '3')
    test_get_all_characters(URL)
