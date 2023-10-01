import requests
import configuration
import sender_stand_request

#функция получения заказа по его номеру
def check_order():
    check_order_response = requests.get(sender_stand_request.check_order_api) # получаем заказ по его номеру, в переменную check_order_response сохраняем ответ
    return check_order_response

# Наталья Бураганова, когорта 08-а — Финальный проект. Инженер по тестированию плюс

# Тест №1. Проверка, что код ответа = 200
def test_status_code():
    assert check_order().status_code == 200



