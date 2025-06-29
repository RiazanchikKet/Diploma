from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from configuration.ConfigProvaider import ConfigProvaider


class Ui:

    def __init__(self, driver):
        """
        Конструктор, открывающий указанный браузер и страницу с указанным в
        конструкторе URL.
        """
        url = ConfigProvaider().get("ui", "base_url")
        self.browser = driver
        self.browser.get(url)

    @allure.step("В поле 'Куда' ввести {where}")
    def field_where(self, where: str) -> None:
        """
        Находит на странице элемент 'Куда' и передает значение, указанное на
        входе при вызове метода.

        Параметры:
        where - название аэропорта или города прибытия
        """
        WebDriverWait(self.browser, 50).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#avia_form_destination-input")
                )
                )
        field = self.browser.find_elements(
            By.CSS_SELECTOR, "#avia_form_destination-input"
            )

        for input_field in field:
            input_field.send_keys(where)
            input_field.send_keys(Keys.RETURN)

    def value_field_where(self) -> str:
        """
        Находит на странице элемент с отображением введенного значения поля\
        'Куда' и выводит его в результате вызова метода.
        """
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#avia_form_destination-input")
                )
                )
        field = self.browser.find_elements(
            By.CSS_SELECTOR, "#avia_form_destination-input"
            )
        for value_field in field:
            result = value_field.get_attribute("value")

        return result
