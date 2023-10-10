from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data
from locators import HeaderLocators, AuthPageLocators, PersonalAccountPageLocators


def test_logout_button(login):
    # Кликнуть на ссылку "Личный Кабинет"
    login.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK).click()
    # Явное ожидание загрузки страницы "Личный Кабинет"
    WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountPageLocators.LOGOUT_BUTTON))
    # Нажать на кнопку "Выход"
    login.find_element(*PersonalAccountPageLocators.LOGOUT_BUTTON).click()
    # Проверка нахождения на странице "Вход" с явным ожиданием загрузки страницы
    assert WebDriverWait(login, 3).until(
        expected_conditions.visibility_of_element_located(AuthPageLocators.SIGN_IN_BUTTON)).text == Data.SIGN_IN_BUTTON_TEXT
