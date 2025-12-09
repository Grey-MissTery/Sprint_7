import random
import string
import allure


@allure.step('Сгенерировать данные курьера')
def generate_couriers_data():
    """Генерирует случайные данные для создания курьера"""
    
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload
