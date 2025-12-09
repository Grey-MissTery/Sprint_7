import sys
import os
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from helpers import generate_couriers_data
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier():
    # Генерируем данные курьера
    courier_data = generate_couriers_data()
    # Создаем курьера
    response = CourierMethods().create_courier(courier_data)
    yield response, courier_data
    # После теста удаляем курьера
    id_courier = CourierMethods().login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    if id_courier[0] == 200:
        CourierMethods().delete_courier(id_courier[1]['id'])


@pytest.fixture
def authorization_courier(courier):
    # Авторизуем курьера
    courier_data = courier[1]
    response = CourierMethods().login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    return response
