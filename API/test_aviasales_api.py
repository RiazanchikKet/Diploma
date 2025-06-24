from api import Api
import allure
import pytest
from config import url, key


@allure.epic("Aviasales")
@allure.title("Получение списка самых дешевых билетов на определенные даты")
@allure.description("Возвращает самые дешевые авиабилеты за определённые даты,\
                    найденные пользователями Авиасейлс за последние 48 часов.")
@allure.feature("Позитивный")
@allure.severity("Blocker")
@pytest.mark.aviasales
@pytest.mark.api
@pytest.mark.api_positive
@pytest.mark.positive
def test_cheap_tickets_for_a_certain_date():
    params = {
        'origin': 'MOW',
        'destination': 'YOW',
        'departure_at': '2025-07-23',
        'unique': 'false',
        'sorting': 'price',
        'direct': 'false',
        'currency': 'rub',
        'limit': 50,
        'page': 1,
        'one_way': 'true',
        'token': key
    }

    api = Api(url)
    result = api.cheap_tickets_for_a_certain_date(params)

    print(f"success = {result['success']}, data = {result['data']}")

    with allure.step(
            "Проверка структуры ответа, результата запроса"
            ):
        assert result['success'] is True
        assert result['data'] is not None
        assert result['currency'] == params['currency']


@allure.epic("Aviasales")
@allure.title("Поиск авиабилетов по цене")
@allure.description("Возвращает авиабилеты в заданном ценовом диапазоне.")
@allure.feature("Позитивный")
@allure.severity("Blocker")
@pytest.mark.aviasales
@pytest.mark.api
@pytest.mark.api_positive
@pytest.mark.positive
def test_search_for_air_tickets_by_price():
    params = {
        'origin': 'MOW',
        'destination': 'LED',
        'value_min': '1000',
        'value_max': '50000',
        'one_way': 'true',
        'direct': 'false',
        'locale': 'ru',
        'currency': 'rub',
        'market': 'ru',
        'limit': 30,
        'page': 1,
        'token': key
    }
    api = Api(url)
    result = api.search_for_air_tickets_by_price(params)

    print(f"success = {result['success']}, data = {result['data']}")

    with allure.step(
            "Проверка структуры ответа, результата запроса"
            ):
        assert result['currency'] == params['currency']
        assert result['data'] is not None
        assert result['success'] is True


@allure.epic("Aviasales")
@allure.title("Цены на авиабилеты за период")
@allure.description("Возвращает цены на авиабилеты за определённый период,\
                    найденные пользователями Авиасейлс за последние 48 часов.")
@allure.feature("Позитивный")
@allure.severity("Blocker")
@pytest.mark.aviasales
@pytest.mark.api
@pytest.mark.api_positive
@pytest.mark.positive
def test_air_ticket_prices_for_the_period():
    params = {
        'currency': 'rub',
        'origin': 'MOW',
        'destination': 'YOW',
        'beginning_of_period': '2025-07-23',
        'period_type': 'year',
        'page': 1,
        'show_to_affiliates': 'true',
        'sorting': 'price',
        'trip_class': 0,
        'token': key
    }
    api = Api(url)
    result = api.air_ticket_prices_for_the_period(params)

    print(f"success = {result['success']}, data = {result['data']}")

    with allure.step(
            "Проверка структуры ответа, результата запроса"
            ):
        assert result['success'] is True
        assert result['data'] is not None


# негативные
@allure.epic("Aviasales")
@allure.title("Получение списка билетов с указанием времени отправления\
              позднее времени прибытия")
@allure.description("Возвращает ошибку 400 и сообщение ошибки. Невозможно\
                    указать дату отправления позднее даты прибытия")
@allure.feature("Негативный")
@allure.severity("Critical")
@pytest.mark.aviasales
@pytest.mark.api
@pytest.mark.api_negative
@pytest.mark.negative
def test_departure_time_later_than_arrival_time():
    params = {
        'origin': 'MOW',
        'destination': 'NQZ',
        'departure_at': '2025-07',
        'return_at': '2025-06',
        'token': key
    }

    api = Api(url)
    result = api.cheap_tickets_for_a_certain_date(params)

    print(f"Сообщение ошибки - {result['error']},\
          код ответа - {result['status']}, success = {result['success']}")

    with allure.step(
            "Проверка структуры ответа, статуса 400, сообщения ошибки ответа"
            ):
        assert result['error'] == \
            'bad request: depart|return min date greater than depart|return max date: invalid params'
        assert result['data'] is None
        assert result['status'] == 400
        assert result['success'] is False


@allure.epic("Aviasales")
@allure.title("Получение списка авиабилетов без указания городов отправления и\
              прибытия")
@allure.description("Возвращает ошибку 400 и сообщение ошибки. Указание одного\
                    из параметров (origin или destination) является\
                    обязательным")
@allure.feature("Негативный")
@allure.severity("Major")
@pytest.mark.aviasales
@pytest.mark.api
@pytest.mark.api_negative
@pytest.mark.negative
def test_departure_and_arrival_cities_are_not_specified():
    params = {
        'departure_at': '2025-08',
        'unique': 'false',
        'sorting': 'price',
        'direct': 'false',
        'currency': 'rub',
        'limit': 50,
        'page': 1,
        'one_way': 'true',
        'token': key
    }

    api = Api(url)
    result = api.cheap_tickets_for_a_certain_date(params)

    print(f"Сообщение ошибки - {result['error']},\
          код ответа - {result['status']}, success = {result['success']}")

    with allure.step(
            "Проверка структуры ответа, статуса 400, сообщения ошибки ответа"
            ):
        assert result['error'] == \
            'bad request: destination: you must set origin either destination.'
        assert result['data'] is None
        assert result['status'] == 400
        assert result['success'] is False
