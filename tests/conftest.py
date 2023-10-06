from random import randint
from faker import Faker
from locators import Locators

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Настройки драйвера
@pytest.fixture
def driver():
    options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    browser.get('https://stellarburgers.nomoreparties.site/')

    yield browser
    browser.quit()


# Генерация случайного пароля
@pytest.fixture
def password():
    password = randint(100000, 9999999)
    return password


# Авторизация зарегистрированного пользователя
@pytest.fixture
def login(driver):
    # Нажать кнопку "Войти в аккаунт"
    driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()
    # Ввод валидных email и пароля
    driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys('test@test.web')
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys('123456')
    # Нажать кнопку "Войти"
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    return driver


# Генерация случайного email
@pytest.fixture
def fake_email():
    faker = Faker()
    fake_email = faker.email()
    return fake_email
