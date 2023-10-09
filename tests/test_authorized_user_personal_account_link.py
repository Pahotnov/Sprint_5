from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Data
from locators import HeaderLocators, PersonalAccountPageLocators


def test_authorized_user_personal_account_link(login):
    # Кликнуть на ссылку "Личный Кабинет"
    login.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK).click()
    # Проверка нахождения на странице "Личный кабинет" с явным ожиданием загрузки страницы
    assert WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountPageLocators.LOGOUT_BUTTON)).text == Data.LOGOUT_BUTTON_TEXT
