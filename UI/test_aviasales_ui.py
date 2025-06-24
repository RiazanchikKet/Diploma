from selenium import webdriver
import allure
import pytest
from ui import Ui
# По заданию необходимо сделать 5 тестов

# Позитивные 3 шт
# 1. Произведен поиск авиабилетов с заполнением всех обязательных полей
# валидными значениями, в билете отображается информация, введенная в
#  поисковике
def test_required_fields_are_filled_in():
    browser = webdriver.Chrome()

    info = Ui(browser)
    info.set_cookie_policy()
    info.fild_where_from("Москва")
    info.fild_where("Калининград")
    info.fild_when()
    info.fild_return()
    info.find_tickets()
    info.choose_a_ticket()
    direction = info.info_ticket()
    date = info.date_ticket()

    print(direction)
    print(date)

    #assert direction == ""
    #assert date == ""

    browser.quit()
test_required_fields_are_filled_in()
# 2. Проверена возможность ввести максимальное кол-во пассажиров "взрослый" - допустимо 9, кнопка "+" становится деактивной
# 3. Проверена возможность купить билет

# Негативные 2 шт
# 1. Проверена возможность указания прошедшей даты в поле даты когда
# 2. Проверена возможность поиска авиабилетов без заполнения полей в поиске

