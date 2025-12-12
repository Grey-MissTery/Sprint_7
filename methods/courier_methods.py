import requests
import allure
from data import *
from helpers import generate_couriers_data


class CourierMethods:
    
    @allure.step('Создать курьера')
    def create_courier(self, params=None):
        if params is None:
            params = generate_couriers_data()
        response = requests.post(COURIERS_URL, data=params)
        return response.status_code, response.json()

    @allure.step('Авторизовать курьера в системе')
    def login_courier(self, params):
        response = requests.post(COURIERS_LOGIN_URL, data=params)
        return response.status_code, response.json()

    def delete_courier(self, id):
        """Служебный метод для удаления курьера (используется в фикстурах)"""
        requests.delete(f'{COURIERS_URL}{id}')
