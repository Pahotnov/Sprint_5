from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


def test_logout_button(login):
    # Кликнуть на ссылку "Личный Кабинет"
    login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
    # Явное ожидание загрузки страницы "Личный Кабинет"
    WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
    # Нажать на кнопку "Выход"
    login.find_element(*Locators.LOGOUT_BUTTON).click()
    # Проверка нахождения на странице "Вход" с явным ожиданием загрузки страницы
    assert WebDriverWait(login, 3).until(
        expected_conditions.visibility_of_element_located(Locators.SIGN_IN_BUTTON)).text == 'Войти'
