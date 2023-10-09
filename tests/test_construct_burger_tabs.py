from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPageLocators


def test_construct_burger_tabs(login):
    # Явное ожидание загрузки страницы "Соберите бургер"
    WebDriverWait(login, 3).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.ASSEMBLE_BURGER_BLOCK))
    # Нажать на табу "Соусы"
    login.find_element(*MainPageLocators.SAUCES_TAB_CLICKABLE).click()
    # Проверка, что таба "Соусы" - активна
    assert 'current' in login.find_element(*MainPageLocators.SAUCES_TAB).get_attribute('class')
    # Нажать на табу "Начинки"
    login.find_element(*MainPageLocators.FILLINGS_TAB_CLICKABLE).click()
    # Проверка, что таба "Начинки" - активна
    assert 'current' in login.find_element(*MainPageLocators.FILLINGS_TAB).get_attribute('class')
    # Нажать на табу "Булки"
    login.find_element(*MainPageLocators.BUNS_TAB_CLICKABLE).click()
    # Проверка, что таба "Булки" - активна
    assert 'current' in login.find_element(*MainPageLocators.BUNS_TAB).get_attribute('class')
