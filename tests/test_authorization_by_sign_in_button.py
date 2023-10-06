from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


def test_authorization_by_sign_in_button(login):
    # Убедиться в наличии кнопки "Оформить заказ" вместо "Войти в аккаунт" с явным ожиданием этой кнопки
    assert WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)).text == 'Оформить заказ'
