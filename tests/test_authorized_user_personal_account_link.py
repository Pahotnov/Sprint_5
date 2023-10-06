from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


def test_authorized_user_personal_account_link(login):
    # Кликнуть на ссылку "Личный Кабинет"
    login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
    # Проверка нахождения на странице "Личный кабинет" с явным ожиданием загрузки страницы
    assert WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON)).text == 'Выход'
