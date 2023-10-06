from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


def test_authorization_by_personal_account_button(driver):
    # Нажать на кнопку "Личный Кабинет"
    driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
    # Ввод валидных email и пароля
    driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys('test@test.web')
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys('123456')
    # Нажать кнопку "Войти"
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    # Явное ожидание загрузки кнопки "Оформить заказ"
    # Убедиться в наличии кнопки "Оформить заказ" вместо "Войти в аккаунт" с явным ожиданием этой кнопки
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)).text == 'Оформить заказ'
