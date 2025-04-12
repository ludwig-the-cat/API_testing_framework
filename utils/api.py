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
