from requests import Response

from conftest import created_place
from utils.api import GoogleMapsAPI

class TestCreatePlace:
    """Создание, изменение и удаление новой локации"""
    def test_create_new_place(self):
        print('Метод POST')
        result_post: Response = GoogleMapsAPI.create_new_place()
        assert result_post.status_code == 200

    def test_check_new_place_is_exist(self, created_place):
        print('Метод GET')
        result_get: Response = GoogleMapsAPI.check_new_location_was_created(place_id=created_place)
        assert result_get.status_code == 200