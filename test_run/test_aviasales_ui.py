from selenium import webdriver
import allure
import pytest
from configuration.ConfigProvaider import ConfigProvaider
from pages.UI.ui import Ui
from pages.UI.passangers import Passengers
from pages.UI.validation import Validation
from pages.UI.date_form import DateForm


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser_name = ConfigProvaider().get("ui", "browser_name")
        if browser_name == 'chrome':
            browser = webdriver.Chrome()
        else:
            browser = webdriver.Firefox()

        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@allure.epic("Aviasales")
@allure.title("Возможно указать минимальное кол-во пассажиров 'Взрослый'\
              (равное 1)")
@allure.description("Проверка граничных значений, возможно указать минимальное\
                    кол-во пассажиров, равное 1")
@allure.feature("Позитивный")
@allure.severity("Critical")
@pytest.mark.aviasales
@pytest.mark.positive
@pytest.mark.ui
@pytest.mark.ui_positive
def test_min_passangers(browser):
    passengers = Passengers(browser)
    passengers.find_passengers()
    button_disabled = passengers.find_minus()
    number_of_passengers = passengers.value_field_passengers()

    print(f"Кнопка '-' активна или нет: true - да, false - нет.\
          Результат: {button_disabled}")
    print(f"Указанное кол-во пассажиров - {number_of_passengers}")

    with allure.step("1. Проверить, что кнопка '-' неактивная и на нее нельзя\
                     нажать;"):
        assert button_disabled is False
    with allure.step("2. Проверить отображение кол-ва пассажиров в табло,\
                     должно отображаться 1"):
        assert number_of_passengers == '1'


@allure.epic("Aviasales")
@allure.title("Возможно указать максимальное кол-во пассажиров 'Взрослый'\
              (равное 9).")
@allure.description("Проверка граничных значений - допустимо указать\
                    максимальное кол-во пассажиров, которое равно 9")
@allure.feature("Позитивный")
@allure.severity("Critical")
@pytest.mark.aviasales
@pytest.mark.positive
@pytest.mark.ui
@pytest.mark.ui_positive
def test_max_passengers(browser):
    passengers = Passengers(browser)
    passengers.find_passengers()
    passengers.click_plus()
    button_disabled = passengers.compare_meaning()
    number_of_passengers = passengers.value_field_passengers()

    print(f"Кнопка '+' активна или нет: true - да, false - нет.\
          Результат: {button_disabled}")
    print(f"Указанное кол-во пассажиров - {number_of_passengers}")

    with allure.step("1. Проверить, что кнопка '+' неактивная и на нее нельзя\
                     нажать;"):
        assert button_disabled is False
    with allure.step("2. Проверить отображение кол-ва пассажиров в табло,\
                     должно измениться с 1 до 9."):
        assert number_of_passengers == '9'


@allure.epic("Aviasales")
@allure.title("Возможно ввести валидное название города в поле 'Куда'")
@allure.description("Проверка, что поле 'Куда' принимает валидные названия\
                    городов.")
@allure.feature("Позитивный")
@allure.severity("Blocker")
@pytest.mark.aviasales
@pytest.mark.positive
@pytest.mark.ui
@pytest.mark.ui_positive
def test_validation_field_where_from(browser):
    search = Ui(browser)
    search.field_where('Новосибирск')
    value_city = search.value_field_where()

    print(f"Указанный город - {value_city}")

    with allure.step("Проверить, что в поле 'Куда' корректно отображается\
                     введенное значение, не вылезает окон с ошибками"):
        assert value_city == 'Новосибирск'


@allure.epic("Aviasales")
@allure.title("Дата прибытия указана раньше, чем дата отправления.")
@allure.description("Проверяем, что невозможно указать в полях 'Куда' и\
                    'Обратно' даты наоборот.")
@allure.feature("Негативный")
@allure.severity("Critical")
@pytest.mark.aviasales
@pytest.mark.negative
@pytest.mark.ui
@pytest.mark.ui_negative
def test_validation_date(browser):
    dates = DateForm(browser)
    dates.field_when()
    dates.field_return()
    value_when = dates.value_field_when()
    value_return = dates.value_field_return()

    print(f" Дата отправления - {value_when}")
    print(f" Дата возвращения - {value_return}")

    with allure.step("Необходимо проверить, что в поле 'Когда' отображается\
                     дата не позднее даты в поле 'Обратно'"):
        with allure.step("Проверить, что в поле 'Когда' корректно отображается\
                         дата"):
            assert value_when == '1 июля, вт'
        with allure.step("Проверить, что в поле 'Когда' корректно отображается\
                         дата"):
            assert value_return == '11 июля, пт'


@allure.epic("Aviasales")
@allure.title("Проверка валидации обязательных полей.")
@allure.description("Проверяем возможность поиска билета без заполнения\
                    обязательных полей. Отображение и текст ошибки.")
@allure.feature("Негативный")
@allure.severity("Major")
@pytest.mark.aviasales
@pytest.mark.negative
@pytest.mark.ui
@pytest.mark.ui_negative
def test_validation_fild(browser):
    field = Validation(browser)
    field.button_find_ticket()
    where = field.field_where()
    when = field.field_when()

    print(f"Текст ошибки в поле 'Куда' - {where}")
    print(f"Текст ошибки в поле 'Когда'{when}")

    with allure.step("Проверить, что в поле 'Куда' и 'Когда' появилось\
                     сообщение об ошибке.'"):
        with allure.step("Проверить, что текст в сообщении ошибки в поле\
                         'Куда' соответствует 'УКАЖИТЕ ГОРОД ПРИБЫТИЯ'"):
            assert where == 'УКАЖИТЕ ГОРОД ПРИБЫТИЯ'
        with allure.step("Проверить, что текст в сообщении ошибки в поле\
                         'Когда' соответствует 'УКАЖИТЕ ДАТУ'"):
            assert when == 'УКАЖИТЕ ДАТУ'
