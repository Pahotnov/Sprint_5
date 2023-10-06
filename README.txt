Проект состоит из 1 папки, содержащей:
1) Файл conftest.py с описанием используемых фикстур.
2) Файлы непосредственно тестов.
А также файла .gitignore и locators, содержащего класс переменных локаторов.
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