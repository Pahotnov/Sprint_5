from locators import Locators


def test_registration_incorrect_password_validation(driver):
    # Регистрация
    driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_LINK) .click()
    # Ввод валидных имени, email, но невалидного пароля
    driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys('Test')
    driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys('test@test.web')
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys('123')
    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    # Проверка срабатывания валидации на невалидный пароль
    assert driver.find_element(*Locators.INCORRECT_PASSWORD_TEXT).text == 'Некорректный пароль'
