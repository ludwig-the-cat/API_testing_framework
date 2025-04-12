from venv import create

from utils.http_methods import HttpMethods

# Определяем базовый URL
BASE_URL = 'https://rahulshettyacademy.com'
# Параметр для всех запросов
KEY='?key=qaclick123'

class GoogleMapsAPI:
    """ Методы для тестирования Google Maps API """

    # Метод для создания новой локации
    @staticmethod
    def create_new_place():
        json_create_new_place = {
                                    "location": {
                                    "lat": -38.383494,
                                    "lng": 33.427362
                                    }, "accuracy": 50,
                                    "name": "Frontline house",
                                    "phone_number": "(+91) 983 893 3937",
                                    "address": "29, side layout, cohen 09",
                                    "types": [
                                     "shoe park",
                                    "shop"
                                     ],
                                    "website": "http://google.com",
                                    "language": "French-IN"
        }
    # Ресурс метода POST
        post_resource = '/maps/api/place/add/json'
        post_url = BASE_URL + post_resource + KEY
        print(post_url)
        result_post = HttpMethods.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

    # Метод проверки существования новой локации
    @staticmethod
    def check_new_location_was_created(place_id):
        get_resource = '/maps/api/place/get/json'
        get_url = BASE_URL + get_resource + KEY + '&place_id=' + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    # Метод обновления локации
    @staticmethod
    def update_location(place_id):

        json_for_update = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        put_resource = '/maps/api/place/update/json'
        put_url = BASE_URL + put_resource + KEY + '&place_id=' + place_id
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_update)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_location(place_id):
        delete_resource = '/maps/api/place/delete/json'
        delete_url = BASE_URL + delete_resource + KEY
        json_to_delete = {
            'place_id': place_id
        }
        print(delete_url)
        result_delete = HttpMethods.post(delete_url, json_to_delete)
        print(result_delete.text)
        return result_delete


