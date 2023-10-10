from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from helpers import Helpers
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators, PersonalAccountPageLocators, \
    HeaderLocators, UnauthorizedUserGeneralLocators


def test_registration_valid_email_and_password(driver):
    fake_email = Helpers.fake_email()
    password = Helpers.password()
    # Регистрация
    driver.find_element(*MainPageLocators.SIGN_IN_ACCOUNT_BUTTON).click()
    driver.find_element(*AuthPageLocators.REGISTRATION_LINK).click()
    # Ввод валидных имени, email, пароля
    driver.find_element(*UnauthorizedUserGeneralLocators.NAME_INPUT_FIELD).send_keys(Data.NAME)
    driver.find_element(*UnauthorizedUserGeneralLocators.EMAIL_INPUT_FIELD).send_keys(fake_email)
    driver.find_element(*UnauthorizedUserGeneralLocators.PASSWORD_INPUT_FIELD).send_keys(password)
    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()
    # Явное ожидание загрузки страницы входа
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(AuthPageLocators.SIGN_IN_BUTTON))
    # Проверка изменения значения лейбла формы на "Вход"
    assert driver.find_element(*AuthPageLocators.SIGN_IN_TITLE).text == Data.SIGN_IN_TITLE_TEXT
    # Ввод email и пароля зарегистрированного пользователя
    driver.find_element(*UnauthorizedUserGeneralLocators.EMAIL_INPUT_FIELD).send_keys(fake_email)
    driver.find_element(*UnauthorizedUserGeneralLocators.PASSWORD_INPUT_FIELD).send_keys(password)
    # Нажать на кнопку "Войти"
    driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON).click()
    # Явное ожидание загрузки кнопки "Оформить заказ" на главной сранице сайта
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.CHECKOUT_BUTTON))
    # Перейти в "Личный Кабинет" с явным ожиданием формы ввода имени, логина и пароля
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(PersonalAccountPageLocators.PROFILE_BLOCK))
    # Проверить, что поле "Имя" содержит значение 'test'
    assert driver.find_element(*PersonalAccountPageLocators.NAME_INPUT).get_attribute('value') == Data.NAME
    # Проверить, что поле "Логин" содержит значение 'test@test.web'
    assert driver.find_element(*PersonalAccountPageLocators.EMAIL_INPUT).get_attribute('value') == fake_email
