from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from configuration.ConfigProvaider import ConfigProvaider


class DateForm:

    def __init__(self, driver):
        """
        Конструктор, открывающий указанный браузер и страницу с указанным в
        конструкторе URL.
        """
        url = ConfigProvaider().get("ui", "base_url")
        self.browser = driver
        self.browser.get(url)

    @allure.step("Найти на странице поле 'Когда' и кликнуть по нему.\
                 В выпадающем боксе выбрать дату 11.07")
    def field_when(self) -> None:
        """
        Находит на странице элемент 'Когда', кликает по нему и в выпадающем
        календаре выбирает дату.
        """
        WebDriverWait(self.browser, 50).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'button[data-test-id="start-date-field"]')
                )
                )
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

    @allure.step("Найти поле 'Обратно', кликнуть по нему и в выпадающем блоке\
                 нажать на 01.07")
    def field_return(self) -> None:
        """
        Находит на странице элемент в календаре со значением 1 июля и нажимает
        на него.
        """
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-test-id="date-01.07.2025"]')
                )
                )
        self.browser.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="date-01.07.2025"]'
            ).click()

    def value_field_when(self) -> str:
        """
        Находит на странице поле 'когда' и выводит значение, указанное в этом
        поле.
        """
        class_date = self.browser.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="start-date-field"]'
            )
        result = class_date.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="start-date-value"]'
        )
        return result.text

    def value_field_return(self) -> str:
        """
        Находит на странице поле 'обратно' и выводит значение, указанное в этом
        поле.
        """
        class_date = self.browser.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="end-date-field"]'
            )
        result = class_date.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="end-date-value"]'
        )
        return result.text
