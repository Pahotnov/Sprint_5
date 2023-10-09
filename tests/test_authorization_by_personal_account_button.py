from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data
from locators import MainPageLocators, HeaderLocators, AuthPageLocators, PersonalAccountPageLocators


def test_authorization_by_personal_account_button(driver):
    # Нажать на кнопку "Личный Кабинет"
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK).click()
    # Ввод валидных email и пароля
    driver.find_element(*AuthPageLocators.EMAIL_INPUT_FIELD).send_keys(Data.EMAIL)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT_FIELD).send_keys(Data.PASSWORD)
    # Нажать кнопку "Войти"
    driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON).click()
    # Убедиться в наличии кнопки "Оформить заказ" вместо "Войти в аккаунт" с явным ожиданием этой кнопки
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.CHECKOUT_BUTTON)).text == Data.CHECKOUT_BUTTON_TEXT
    # Перейти в "Личный Кабинет" с явным ожиданием формы ввода имени, логина и пароля
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(PersonalAccountPageLocators.PROFILE_BLOCK))
    # Проверить, что поле "Имя" содержит значение 'test'
    assert driver.find_element(*PersonalAccountPageLocators.NAME_INPUT).get_attribute('value') == Data.NAME
    # Проверить, что поле "Логин" содержит значение 'test@test.web'
    assert driver.find_element(*PersonalAccountPageLocators.EMAIL_INPUT).get_attribute('value') == Data.EMAIL
