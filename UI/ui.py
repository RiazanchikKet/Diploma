from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Ui:

    def __init__(self, driver):
        """
        Конструктор, открывающий указанный браузер и страницу с указанным в
        конструкторе URL.
        """
        self.browser = driver
        self.browser.get(
            "https://www.aviasales.ru/"
            )
        self.browser.maximize_window()
        self.browser.implicitly_wait(20)

    def set_cookie_policy(self):
        cookie = {
            "name": "cookie_policy",
            "value": "%7B%22accepted%22%3Atrue%2C%22technical%22%3Atrue%2C%22marketing%22%3Atrue%7D"
        }
        self.browser.add_cookie(cookie)

    # -Найти элемент откуда
    @allure.step("В поле 'Откуда' ввести {where_from}")
    def fild_where_from(self, where_from: str) -> None:
        """
        Ожидает загрузки страницы, находит элемент 'Откуда' на странице и
        передает значение, указанное на входе при вызове метода.

        Параметры:
        where_from - название аэропорта города отправления, передающееся при
        вызове метода.
        """

        WebDriverWait(self.browser, 50).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#avia_form_origin-input")
                )
                )
        fild = self.browser.find_elements(
            By.CSS_SELECTOR, "#avia_form_origin-input"
            )
        for input_where_from in fild:
            input_where_from.clear()
            input_where_from.send_keys(where_from)
            input_where_from.send_keys(Keys.RETURN)

    # -Найти элемент куда
    @allure.step("В поле 'Куда' ввести {where}")
    def fild_where(self, where: str) -> None:
        """
        Находит на странице элемент 'Куда' и передает значение, указанное на
        входе при вызове метода.

        Параметры:
        where - название аэропорта или города прибытия
        """
        fild = self.browser.find_elements(
            By.CSS_SELECTOR, "#avia_form_destination-input"
            )
        
        for input_fild in fild:
            input_fild.send_keys(where)
            input_fild.send_keys(Keys.RETURN)

    # -Найти элемент когда
    @allure.step("")
    def fild_when(self) -> None:
        """
        Находит на странице элемент 'Когда', кликает по нему и в выпадающем
        календаре выбирает дату.
        """
        self.browser.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="start-date-field"]'
            ).click()
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-test-id="date-11.07.2025"]')
                )
                )
        self.browser.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="date-11.07.2025"]'
            ).click()

    @allure.step("Нажать на кнопку 'Обратный билет не нужен'")
    def fild_return(self) -> None:
        """
        В выпадающем календаре в поле 'Обратно' нажимает на кнопку
        'Обратный билет не нужен'.
        """
        self.browser.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="calendar-action-button"]'
            ).click()

    # -Найти элемент "найти билеты" - нажать
        # -выставить явное ожидание для загрузки страницы (тут заканчивается первый тест)
    @allure.step("Нажать на кнопку 'Найти билеты'")
    def find_tickets(self) -> None:
        """
        Находит на странице элемент 'Найти билеты' и нажимает на него.
        Ожидает прогрузки страницы с информацией о билетах.
        """
        self.browser.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="form-submit"]'
            ).click()


    # -выставить ожидание для загрузки страницы
    # -найти элемент с билетом для его просмотра, нажать на "выбрать билет"
    @allure.step("Выбрать любой билет из списка и нажать на него или на кнопку\
                 'Выбрать билет'")
    def choose_a_ticket(self) -> None:
        """
        Ожидает прогрузки страницы и находит контейнер с билетами
        """
        WebDriverWait(self.browser, 60).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR,
                    'div div[data-test-id="ticket-preview"]')
            )
                )
        self.browser.execute_script("window.scrollBy(0, 1000);")
        tickets = self.browser.find_elements(
            By.CSS_SELECTOR, 'div[data-test-id="ticket-preview"]'
            )
        
        for ticket in tickets:
            ticket[0].send_keys(Keys.PAGE_DOWN)
            ticket[0].find_element(
                By.CSS_SELECTOR, "button[data-test-id='button']"
                ).click()

    # -выставить ожидания для загрузки информации по билету (тут заканчивается\
    # второй тест, необходимо будет сделать проверку по информации, что будет\
    # видна в билете)
    @allure.step("Дождаться загрузки информации по билету и сравнить...")
    def info_ticket(self) -> str:
        """
        
        """
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                    'div.s__iGIjimcU_s_88XPQORGB[data-test-id="text"]')
                )
                )
        info_ticket = self.browser.find_element(
            By.CSS_SELECTOR, 
            'div.s__iGIjimcU_s_88XPQORGB[data-test-id="text"]'
            )
        return info_ticket.text

    @allure.step("")
    def date_ticket(self) -> str:
        """
        
        """
        class_date = self.browser.find_element(
            By.CSS_SELECTOR,
            "div.s__rPrqV3cL3bPhiydyeWcD.s__h1kFjuR6mPMHAQ2LyBV7"
        )
        date = class_date.find_element(
            By.CSS_SELECTOR,
            "div.s__fDJ19GJO9BCkieSYidFs"
        )
        return date.text

    # -найти элемент "купить" (заканчивается 3-я проверка)
