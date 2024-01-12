#Розалия Жарасова, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

# Клиент создает заказ.
def create_order(body):
    return requests.post (configuration.BASE_URL + configuration.CREAT_ORDERS,
                         json=body)

# Проверяется, что по треку заказа можно получить данные о заказе.
def get_order(track):
    return requests.get(f'{configuration.BASE_URL}{configuration.CREAT_ORDERS}', params = track)