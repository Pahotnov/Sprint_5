from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data
from locators import MainPageLocators


def test_authorization_by_sign_in_button(login):
    # Убедиться в наличии кнопки "Оформить заказ" вместо "Войти в аккаунт" с явным ожиданием этой кнопки
    assert WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.CHECKOUT_BUTTON)).text == Data.CHECKOUT_BUTTON_TEXT
