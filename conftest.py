from data import Data
from locators import MainPageLocators, AuthPageLocators, UnauthorizedUserGeneralLocators
import pytest
from selenium import webdriver
from urls import Urls


# Настройки драйвера
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.MAIN_URL)

    yield driver
    driver.quit()


# Авторизация зарегистрированного пользователя
@pytest.fixture
def login(driver):
    # Нажать кнопку "Войти в аккаунт"
    driver.find_element(*MainPageLocators.SIGN_IN_ACCOUNT_BUTTON).click()
    # Ввод валидных email и пароля
    driver.find_element(*UnauthorizedUserGeneralLocators.EMAIL_INPUT_FIELD).send_keys(Data.EMAIL)
    driver.find_element(*UnauthorizedUserGeneralLocators.PASSWORD_INPUT_FIELD).send_keys(Data.PASSWORD)
    # Нажать кнопку "Войти"
    driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON).click()
    return driver
