from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


def test_registration_valid_email_and_password(driver, fake_email, password):
    # Регистрация
    driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_LINK) .click()
    # Ввод валидных имени, email, пароля
    driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys('Test')
    driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(fake_email)
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password)
    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    # Явное ожидание загрузки страницы входа
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.SIGN_IN_BUTTON))
    # Проверка изменения значения лейбла формы на "Вход"
    assert driver.find_element(*Locators.SIGN_IN_TITLE).text == 'Вход'
    # Закрыть браузер
    driver.quit()
