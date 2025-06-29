import requests
import allure


class Api:

    def __init__(self, url):
        """
        Конструктор принимающий на вход URL страницы, на которую будет
        отправлен запрос.
        """
        self.url = url

    @allure.step("Отправить GET запрос на ручку /aviasales/v3/prices_for_dates\
        с указанием параметров {params}")
    def cheap_tickets_for_a_certain_date(self, params: dict) -> dict:
        """
        GET запрос возвращает самые дешевые авиабилеты за определённые даты,
        найденные пользователями Авиасейлс за последние 48 часов.

        Параметры:
        params - параметры переданые на вход при вызове метода в виде
        словаря, необходимые для осуществления запроса.

        Например:
        - currency — валюта цен на билеты. Значение по умолчанию — rub.
        - origin — пункт отправления. IATA-код города или аэропорта. Длина не
        менее двух и не более трёх символов. Необходимо указать, если нет
        destination.
        - destination — пункт назначения. IATA-код города или аэропорта. Длина
        не менее двух и не более трёх. Необходимо указать, если нет origin.
        departure_at (необязательно)— дата вылета из пункта отправления (в
        формате YYYY-MM или YYYY-MM-DD).
        - return_at (необязательно) — дата возвращения. Чтобы получить билеты
        в один конец, оставьте это поле пустым.
        - one_way (необязательно) — билет в одну сторону. Принимает значения
        true или false. По умолчанию true. Поскольку в запросе применяется
        группировка по датам, при значении true возвращается только 1 билет в
        одну сторону. Чтобы получить больше билетов в обе стороны, используйте
        one_way=false.
        - direct — получить рейсы без пересадок. Принимает значения true или
        false. По умолчанию false.
        - market — задаёт маркет источника данных (по умолчанию ru).
        - limit — количество записей в ответе. Значение по умолчанию — 30. Не
        более 1000.
        - page — номер страницы. Используется, чтобы пропустить первые записи.
        То есть, выдача будет отдавать билеты в диапазоне
        [(page — 1) * limit; page * limit]. Таким образом, если мы хотим
        получить билеты с 100 по 150, то мы должны установить page=3,
        а limit=50.
        - sorting — сортировка цен:
            - price — по цене (значение по умолчанию).
            - route — по популярности маршрута.
        - unique — возвращает только уникальные направления, если был указан
        origin, но не указан destination. Позволяет собрать топ самых дешевых
        билетов из указанного города. Принимает значения true или false. По
        умолчанию false.
        - token - это индивидуальный ключ (обязательно).
        """
        resp = requests.get(
            self.url+'prices_for_dates?', params
            )
        return resp.json()

    @allure.step("Отправить GET запрос на ручку\
        /aviasales/v3/search_by_price_range с указанием параметров {params}")
    def search_for_air_tickets_by_price(self, params: dict) -> dict:
        """
        GET запрос возвращает авиабилеты в заданном ценовом диапазоне.

        Параметры:
        params - параметры переданые на вход при вызове метода в виде
        словаря, необходимые для осуществления запроса.

        Например:
        - origin — IATA-код аэропорта отправления.
        - destination — IATA-код аэропорта прибытия.
        - value_min — минимальная стоимость билета.
        - value_min — минимальная стоимость билета.
        - value_max — максимальная стоимость билета.
        - one_way — перелёт в один конец:
            - true – только в одну сторону,
            - false – туда-обратно.
        - direct — прямые рейсы: true – только без пересадок, false – с
        пересадками (по умолчанию false).
        - locale — язык ответа (ru – русский).
        - currency — валюта, в которой отображаются цены (rub – российские
        рубли).
        - market — определяет источник данных (по умолчанию ru).
        - limit — количество записей на странице.
        - page — номер страницы (используется для получения ограниченного
        количества результатов).
        - token - это индивидуальный ключ (обязательно).
        """
        resp = requests.get(self.url+'search_by_price_range?', params)
        return resp.json()

    @allure.step("Отправить GET запрос на ручку\
        /aviasales/v3/get_latest_prices с указанием параметров {params}")
    def air_ticket_prices_for_the_period(self, params: dict) -> dict:
        """
        GET запрос. Возвращает цены на авиабилеты за определённый период,
        найденные пользователями Авиасейлс за последние 48 часов.

        Параметры:
        params - параметры переданые на вход при вызове метода в виде
        словаря, необходимые для осуществления запроса.

        Например:
        - currency — валюта цен на билеты. Значение по умолчанию — rub.
        - origin — пункт отправления. IATA-код страны, города или аэропорта.
        Длина не менее двух и не более трёх символов.
        - destination — пункт назначения. IATA-код страны, города или
        аэропорта. Длина не менее двух и не более трёх.
        Если origin и destination не указаны, по умолчанию будет возвращаться
        origin=MOW.
        - beginning_of_period — начало периода даты вылета.
        - period_type — период, в котором искали билеты. Если период не
        указан, то отображаются билеты для перелётов в текущем месяце:
            - year — билеты, найденные в указанном году. В beginning_of_period
            год указывается в формате YYYY;
            - month — билеты за указанный в beginning_of_period месяц (месяц в
            формате YYYY-MM-DD);
            - day — билеты за указанный в beginning_of_period день (день в
            формате YYYY-MM-DD).
        - group_by — параметр группировки:
        - dates — по датам (по умолчанию);
        - directions — по направлениям.
        - one_way — true — в одну сторону, false — туда и обратно. Значение по
        умолчанию — true.
        - page — номер страницы. Значение по умолчанию — 1.
        - market — задаёт маркет источника данных (по умолчанию ru).
        - sorting — сортировка цен:
            - price — по цене (значение по умолчанию). Для направлений город —
            город возможна сортировка только по цене.
            - route — по популярности маршрута.
        - distance_unit_price — по цене за километр.
        - trip_duration — длительность путешествия в днях.
        - trip_class — класс обслуживания самолёте:
            - 0 — эконом;
            - 1 — бизнес класс;
            - 2 — первый класс.
        - token - это индивидуальный ключ (обязательно).
        """
        resp = requests.get(self.url+'get_latest_prices?', params)
        return resp.json()
