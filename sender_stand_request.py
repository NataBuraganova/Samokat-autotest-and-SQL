import configuration
import data
import requests

# функция получения номера нового заказа
def track ():
    # создаем заказ и сохраняем ответ в переменную response_post_new_order
    response_post_new_order = requests.post(configuration.URL_SERVISE + configuration.CREATE_ORDERS,
                                            json = data.order_body)
    track= response_post_new_order.json() # переводим ответ в фомат словаря
    track_value = track ['track'] # в переменную track_value сохраняем значение 'track'
    return track_value


track_value = str(track()) # переводим значение токена в тип строка

check_order_api = configuration.URL_SERVISE + configuration.CHECK_ORDER + track_value # api адрес запросв на получение заказа по трек номеру

