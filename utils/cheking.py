from requests import Response


class Cheking:
    """ Храним методы проверки правильности выполнения запросов"""
    # Проверяем статус коды
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert response.status_code == status_code, 'Статус код неправильный'
