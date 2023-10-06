from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


def test_authorized_user_constructor_link_from_personal_account_form(login):
    # Кликнуть на ссылку "Личный Кабинет"
    login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
    # Кликнуть на ссылку "Конструктор"
    login.find_element(*Locators.CONSTRUCTOR_LINK).click()
    # Явное ожидание загрузки страницы "Соберите бургер"
    assert WebDriverWait(login, 3).until(
        expected_conditions.visibility_of_element_located(Locators.ASSEMBLE_BURGER_BLOCK))
    # Убедиться в наличии кнопки "Оформить заказ" вместо "Войти в аккаунт" с явным ожиданием этой кнопки
    assert WebDriverWait(login, 3).until(
        expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)).text == 'Оформить заказ'