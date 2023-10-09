from data import Data
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators


def test_registration_incorrect_password_validation(driver):
    # Регистрация
    driver.find_element(*MainPageLocators.SIGN_IN_ACCOUNT_BUTTON).click()
    driver.find_element(*AuthPageLocators.REGISTRATION_LINK).click()
    # Ввод валидных имени, email, но невалидного пароля
    driver.find_element(*RegistrationPageLocators.NAME_INPUT_FIELD).send_keys()
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT_FIELD).send_keys(Data.EMAIL)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT_FIELD).send_keys(Data.INCORRECT_PASSWORD)
    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()
    # Проверка срабатывания валидации на невалидный пароль
    assert driver.find_element(*RegistrationPageLocators.INCORRECT_PASSWORD_TEXT).text == Data.INCORRECT_PASSWORD_VALIDATION_TEXT
