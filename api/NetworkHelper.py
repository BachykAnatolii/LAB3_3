import requests
from requests.auth import HTTPBasicAuth

class NetworkHelper:
    BASE_URL = 'http://127.0.0.1:8000'
    USERNAME = 'Yevhenii'
    PASSWORD = '123321A10123'

    @staticmethod
    def get_auth():
        """Повертає об'єкт HTTPBasicAuth для аутентифікації."""
        return HTTPBasicAuth(NetworkHelper.USERNAME, NetworkHelper.PASSWORD)

    @staticmethod
    def get_positions():
        response = requests.get(f"{NetworkHelper.BASE_URL}/positions/", auth=NetworkHelper.get_auth())
        response.raise_for_status()  # Перевірка на помилки
        return response.json()

    @staticmethod
    def get_position_by_id(position_id):
        response = requests.get(f"{NetworkHelper.BASE_URL}/positions/{position_id}/", auth=NetworkHelper.get_auth())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def create_position(data):
        response = requests.post(f"{NetworkHelper.BASE_URL}/positions/", json=data, auth=NetworkHelper.get_auth())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def update_position(position_id, data):
        response = requests.put(f"{NetworkHelper.BASE_URL}/positions/{position_id}/", json=data, auth=NetworkHelper.get_auth())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_position(position_id):
        response = requests.delete(f"{NetworkHelper.BASE_URL}/positions/{position_id}/", auth=NetworkHelper.get_auth())
        response.raise_for_status()
        return response.status_code == 204
