from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data
from locators import MainPageLocators, AuthPageLocators, UnauthorizedUserGeneralLocators


def test_authorization_by_sign_in_link_from_registration_form(driver):
    # Регистрация
    driver.find_element(*MainPageLocators.SIGN_IN_ACCOUNT_BUTTON).click()
    driver.find_element(*AuthPageLocators.REGISTRATION_LINK).click()
    # Нажать ссылку "Войти"
    driver.find_element(*UnauthorizedUserGeneralLocators.SIGN_IN_LINK).click()
    # Ввод валидных email и пароля
    driver.find_element(*UnauthorizedUserGeneralLocators.EMAIL_INPUT_FIELD).send_keys(Data.EMAIL)
    driver.find_element(*UnauthorizedUserGeneralLocators.PASSWORD_INPUT_FIELD).send_keys(Data.PASSWORD)
    # Нажать кнопку "Войти"
    driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON).click()
    # Убедиться в наличии кнопки "Оформить заказ" вместо "Войти в аккаунт" с явным ожиданием этой кнопки
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.CHECKOUT_BUTTON)).text == Data.CHECKOUT_BUTTON_TEXT
