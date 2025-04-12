import requests

class HttpMethods:
    """Определяем методы для работы с API"""
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @classmethod
    def get(cls, url):
        result = requests.get(url=url, headers=cls.headers, cookies=cls.cookie)
        return  result

    @classmethod
    def post(cls, url, body):
        result = requests.post(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
        return result

    @classmethod
    def put(cls, url, body):
        result = requests.put(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
        return result

    @classmethod
    def delete(cls, url, body):
        result = requests.delete(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
        return result