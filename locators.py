from selenium.webdriver.common.by import By


class Locators:
    SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/account"]')  # ссылка "Личный кабинет"
    NAME_INPUT_FIELD = (By.XPATH, './/label[text()="Имя"]/following-sibling::input')  # поле ввода имени
    EMAIL_INPUT_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input')  # поле ввода email
    PASSWORD_INPUT_FIELD = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')  # поле ввода пароля
    REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # кнопка "Зарегистрироваться"
    SIGN_IN_LINK = (By.CSS_SELECTOR, 'a[href="/login"]')  # ссылка "Войти"
    INCORRECT_PASSWORD_TEXT = (By.CSS_SELECTOR, 'p[class*="input__error"]')  # валидация при вводе некорректного пароля
    SIGN_IN_TITLE = (By.CSS_SELECTOR, 'div[class*="Auth_login"]>h2')  # заголовок страницы "Вход"
    SIGN_IN_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # кнопка "Войти"
    REGISTRATION_LINK = (By.CSS_SELECTOR, 'a[href="/register"]')  # ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')  # ссылка "Восстановить пароль"
    FORGOT_PASSWORD_BUTTON = (By.XPATH, './/button[text()="Восстановить"]')  # кнопка "Восстановить"
    CHECKOUT_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')  # кнопка "Выход"
    CONSTRUCTOR_LINK = (By.XPATH, './/p[text()="Конструктор"]')  # ссылка "Конструктор"
    ASSEMBLE_BURGER_BLOCK = (By.CSS_SELECTOR, 'section[class*="BurgerIngredients"]')  # блок "Соберите бургер"
    LOGO_LINK = (By.CSS_SELECTOR, 'div[class*="logo"]>a[href="/"]')  # ссылка лого
    BUNS_TAB = (By.XPATH, './/span[text()="Булки"]/parent::div')  # таба "Булки"
    SAUCES_TAB = (By.XPATH, './/span[text()="Соусы"]/parent::div')  # таба "Соусы"
    FILLINGS_TAB = (By.XPATH, './/span[text()="Начинки"]/parent::div')  # таба "Начинки"
    BUNS_TAB_CLICKABLE = (By.XPATH, './/span[text()="Булки"]')  # таба "Булки"
    SAUCES_TAB_CLICKABLE = (By.XPATH, './/span[text()="Соусы"]')  # таба "Соусы"
    FILLINGS_TAB_CLICKABLE = (By.XPATH, './/span[text()="Начинки"]')  # таба "Начинки"