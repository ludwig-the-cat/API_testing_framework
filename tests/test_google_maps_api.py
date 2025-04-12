from requests import Response

from utils.api import GoogleMapsAPI

class TestCreatePlace:
    """Создание, изменение и удаление новой локации"""
    def test_create_new_place(self):
        print('Метод POST')
        result_post: Response = GoogleMapsAPI.create_new_place()