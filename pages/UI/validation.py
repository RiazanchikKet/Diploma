from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from configuration.ConfigProvaider import ConfigProvaider


class Validation:

    def __init__(self, driver):
        """
        Конструктор, открывающий указанный браузер и страницу с указанным в
        конструкторе URL.
        """
        url = ConfigProvaider().get("ui", "base_url")
        self.browser = driver
        self.browser.get(url)

    @allure.step("Нажать на кнопку 'Найти билеты'")
    def button_find_ticket(self) -> None:
        """
        Находит на странице элемент 'Найти билеты' и нажимает на него.
        Ожидает прогрузки страницы с информацией о билетах.
        """
        WebDriverWait(self.browser, 50).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'button[data-test-id="form-submit"]')
                )
                )
        self.browser.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="form-submit"]'
            ).click()

    def field_where(self) -> str:
        """
        Находит на странице окно с ошибкой у поля 'Куда' и выводит ее значение.
        """
        class_destination_label = self.browser.find_element(
            By.CSS_SELECTOR,
            'div[aria-labelledby="avia_form_destination-label"]'
            )
        message = class_destination_label.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="text"]'
        )
        return message.text

    def field_when(self) -> str:
        """
        Находит на странице окно с ошибкой у поля 'Когда' и выводит ее
        значение.
        """
        class_start_date = self.browser.find_element(
            By.CSS_SELECTOR, 'div button[data-test-id="start-date-field"]'
            )
        message = class_start_date.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="text"]'
            )
        return message.text
