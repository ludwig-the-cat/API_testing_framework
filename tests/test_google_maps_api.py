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

    def test_update_created_location(self, created_place):
        print('Метод PUT')
        result_put = GoogleMapsAPI.update_location(place_id=created_place)
        assert result_put.status_code == 200
        msg = result_put.json()
        assert msg.get('msg') == 'Address successfully updated'
        new_address_check = GoogleMapsAPI.check_new_location_was_created(place_id=created_place).json()
        assert new_address_check.get('address') == '100 Lenina street, RU', 'Address not updated'

    def test_deleting_of_new_place(self, created_place):
        print('Метод Delete')
        result_delete = GoogleMapsAPI.delete_new_location(place_id=created_place)
        msg = result_delete.json()
        assert result_delete.status_code == 200
        assert msg.get('status') == 'OK'