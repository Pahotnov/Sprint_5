from selenium.webdriver.common.by import By


class UnauthorizedUserGeneralLocators:
    EMAIL_INPUT_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input')  # поле ввода email
    PASSWORD_INPUT_FIELD = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')  # поле ввода пароля
    SIGN_IN_LINK = (By.CSS_SELECTOR, 'a[href="/login"]')  # ссылка "Войти"


class MainPageLocators:
    SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт"
    CHECKOUT_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"
    ASSEMBLE_BURGER_BLOCK = (By.CSS_SELECTOR, 'section[class*="BurgerIngredients"]')  # блок "Соберите бургер"
    BUNS_TAB = (By.XPATH, './/span[text()="Булки"]/parent::div')  # таба "Булки"
    SAUCES_TAB = (By.XPATH, './/span[text()="Соусы"]/parent::div')  # таба "Соусы"
    FILLINGS_TAB = (By.XPATH, './/span[text()="Начинки"]/parent::div')  # таба "Начинки"
    BUNS_TAB_CLICKABLE = (By.XPATH, './/span[text()="Булки"]')  # таба "Булки" (кликабельная)
    SAUCES_TAB_CLICKABLE = (By.XPATH, './/span[text()="Соусы"]')  # таба "Соусы" (кликабельная)
    FILLINGS_TAB_CLICKABLE = (By.XPATH, './/span[text()="Начинки"]')  # таба "Начинки" (кликабельная)


class HeaderLocators:
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/account"]')  # ссылка "Личный кабинет"
    CONSTRUCTOR_LINK = (By.XPATH, './/p[text()="Конструктор"]')  # ссылка "Конструктор"
    LOGO_LINK = (By.CSS_SELECTOR, 'div[class*="logo"]>a[href="/"]')  # ссылка лого


class AuthPageLocators:
    SIGN_IN_TITLE = (By.CSS_SELECTOR, 'div[class*="Auth_login"]>h2')  # заголовок страницы "Вход"
    SIGN_IN_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # кнопка "Войти"
    REGISTRATION_LINK = (By.CSS_SELECTOR, 'a[href="/register"]')  # ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')  # ссылка "Восстановить пароль"


class RegistrationPageLocators:
    NAME_INPUT_FIELD = (By.XPATH, './/label[text()="Имя"]/following-sibling::input')  # поле ввода имени
    REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # кнопка "Зарегистрироваться"
    INCORRECT_PASSWORD_TEXT = (By.CSS_SELECTOR, 'p[class*="input__error"]')  # валидация при вводе некорректного пароля


class ForgotPasswordPageLocators:
    FORGOT_PASSWORD_BUTTON = (By.XPATH, './/button[text()="Восстановить"]')  # кнопка "Восстановить"


class PersonalAccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')  # кнопка "Выход"
    PROFILE_BLOCK = (By.CSS_SELECTOR, 'div[class*="Profile_profile"]') # блок пользовательских данных
    NAME_INPUT = (By.XPATH, './/label[text()="Имя"]/following-sibling::input') # поле "Имя"
    EMAIL_INPUT = (By.XPATH, './/label[text()="Логин"]/following-sibling::input')  # поле "Логин"
