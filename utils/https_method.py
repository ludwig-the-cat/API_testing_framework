import requests

class HttpMethods:
    """ Список HTTP методов для вызова """
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @classmethod
    def get(cls, url):
        return requests.get(url=url, headers=cls.headers, cookies=cls.cookie)

    @classmethod
    def post(cls, url, body):
        return requests.post(url=url, headers=cls.headers, cookies=cls.cookie, json=body)

    @classmethod
    def put(cls, url, body):
        return requests.put(url=url, headers=cls.headers, cookies=cls.cookie, json=body)

    @classmethod
    def patch(cls, url, body):
        return requests.patch(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
