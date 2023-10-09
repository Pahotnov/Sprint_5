from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data
from locators import MainPageLocators, HeaderLocators


def test_authorized_user_logo_link_from_personal_account_form(login):
    # Кликнуть на ссылку "Личный Кабинет"
    login.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK).click()
    # Кликнуть на ссылку лого
    login.find_element(*HeaderLocators.LOGO_LINK).click()
    # Явное ожидание загрузки страницы "Соберите бургер"
    assert WebDriverWait(login, 3).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.ASSEMBLE_BURGER_BLOCK))
    # Убедиться в наличии кнопки "Оформить заказ" вместо "Войти в аккаунт" с явным ожиданием этой кнопки
    assert WebDriverWait(login, 3).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.CHECKOUT_BUTTON)).text == Data.CHECKOUT_BUTTON_TEXT
