from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


def test_authorization_by_sign_in_link_from_forgot_password_form(driver):
    # Нажать кнопку "Войти в аккаунт"
    driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()
    # Нажать ссылку "Восстановить пароль"
    driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
    # Нажать ссылку "Войти"
    driver.find_element(*Locators.SIGN_IN_LINK).click()
    # Явное ожидание загрузки страницы входа
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.SIGN_IN_BUTTON))
    # Ввод валидных email и пароля
    driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys('test@test.web')
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys('123456')
    # Нажать кнопку "Войти"
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    # Убедиться в наличии кнопки "Оформить заказ" вместо "Войти в аккаунт" с явным ожиданием этой кнопки
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)).text == 'Оформить заказ'
