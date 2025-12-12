import sys
import os
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from helpers import generate_couriers_data
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier():
    # Генерируем данные курьера, НЕ создаём курьера
    courier_data = generate_couriers_data()
    yield courier_data  # Возвращаем только данные
    
    # После теста: если курьер был создан - удаляем его
    try:
        id_courier = CourierMethods().login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        if id_courier[0] == 200:
            CourierMethods().delete_courier(id_courier[1]['id'])
    except:
        pass  # Если курьер не был создан - ничего не делаем


@pytest.fixture
def authorization_courier(courier):
    # Получаем данные курьера из фикстуры courier
    courier_data = courier
    
    # 1. Создаём курьера (это происходит в тесте, не в фикстуре)
    CourierMethods().create_courier(courier_data)
    
    # 2. Авторизуемся и возвращаем результат
    response = CourierMethods().login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    
    return response
