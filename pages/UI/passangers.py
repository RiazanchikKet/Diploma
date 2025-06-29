from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from configuration.ConfigProvaider import ConfigProvaider


class Passengers:

    def __init__(self, driver):
        """
        Конструктор, открывающий указанный браузер и страницу с указанным в
        конструкторе URL.
        """
        url = ConfigProvaider().get("ui", "base_url")
        self.browser = driver
        self.browser.get(url)

    @allure.step("Найти на старнице поле с указанием пассажиров и кликнуть по\
                 нему")
    def find_passengers(self) -> None:
        """
        Ожидает загрузки страницы. Находит на странице элемент '1 пассажир' и
        кликает по нему.
        """
        WebDriverWait(self.browser, 50).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                    'div button[data-test-id="passengers-field"]')
                )
                )
        self.browser.find_element(
            By.CSS_SELECTOR, 'div button[data-test-id="passengers-field"]'
            ).click()

    @allure.step("В выпадающем списке нажать на '+' у 'взрослый' 8 раз")
    def click_plus(self) -> None:
        class_adult = self.browser.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="number-of-adults"]'
            )
        button = class_adult.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="increase-button"]'
        )
        button.click()
        button.click()
        button.click()
        button.click()
        button.click()
        button.click()
        button.click()
        button.click()

    def compare_meaning(self) -> bool:
        """
        Находит на странице элемент '+' у 'взрослый' и проверяет на
        доступность взаимодействия с кнопкой.
        """
        class_adult = self.browser.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="number-of-adults"]'
            )
        button = class_adult.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="increase-button"]'
        ).is_enabled()

        return button

    def find_minus(self) -> bool:
        """
        Находит на странице элемент '+' у 'взрослый' и проверяет на
        доступность взаимодействия с кнопкой.
        """
        class_adult = self.browser.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="number-of-adults"]'
        )
        button = class_adult.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="decrease-button"]'
        ).is_enabled()

        return button

    def value_field_passengers(self) -> str:
        """
        Находит на странице элемент отображения кол-ва пассажиров и выводит
        его результат.
        """
        class_adult = self.browser.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="number-of-adults"]'
        )
        result = class_adult.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="passenger-number"]'
        )

        return result.text
