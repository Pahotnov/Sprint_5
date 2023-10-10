Проект состоит из 1 папки tests, содержащей тесты, и файлов:
1) .gitignore.py
2) conftest.py - содержит фикстуры driver и login
3) data.py - содержит статичные тестовые данные
4) helpers.py - содержит вспомогательные методы для создания фейкового email и генерации валидного пароля
5) locators.py - содержит классы с переменными локаторов
6) README.txt - собственно, описание проекта
7) urls.py - содержит переменную со значением url тестируемого сайта

Реализованы следующие тесты:
1. test_authorization_by_personal_account_button - вход через кнопку «Личный кабинет»
2. test_authorization_by_sign_in_button - вход по кнопке «Войти в аккаунт» на главной
3. test_authorization_by_sign_in_link_from_forgot_password_form - вход через кнопку в форме восстановления пароля
4. test_authorization_by_sign_in_link_from_registration_form - вход через кнопку в форме регистрации
5. test_authorized_user_constructor_link_from_personal_account_form - проверка перехода по клику на «Конструктор»
6. test_authorized_user_logo_link_from_personal_account_form - проверка перехода по клику на логотип Stellar Burgers
7. test_authorized_user_personal_account_link - проверка перехода по клику на «Личный кабинет»
8. test_construct_burger_tabs - проверка, что работают переходы к разделам: «Булки», «Соусы», «Начинки»
9. test_logout_button - проверка выхода по кнопке «Выйти» в личном кабинете
10. test_registration_incorrect_password_validation - проверка неуспешной регистрации при некорректном пароле
11. test_registration_valid_email_and_password - проверка успешной регистрации

Используются следующие библиотеки:
expected_conditions - для выполнения определённых условий. Используется в связке с WebDriverWait
WebDriverWait - для ожидания выполнения определённых условий. Используется в связке с expected_conditions
Data - класс статичных данных
Helpers - класс методов для создания фейкового email и генерации валидного пароля. Содержит модули Faker и randint.
MainPageLocators, AuthPageLocators, RegistrationPageLocators, PersonalAccountPageLocators, HeaderLocators, PersonalAccountPageLocators - классы с переменными локаторов
By - для выполнения поиска по заданному локатору
Urls - для импорта переменной со значением url тестируемого сайта