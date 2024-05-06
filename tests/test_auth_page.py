from pages.auth_page import AuthPage
import time
from pages.conftests import *
from pages.locators import AuthLocators


def test_auth_page_phone(selenium):
    page = AuthPage(selenium)
    page.enter_phone("89112642210")
    page.enter_pass("N123456n")
    time.sleep(5)
    page.btn_click()
    time.sleep(5)


def test_auth_page_email(selenium):
    page = AuthPage(selenium)
    page.email_btn_click()
    page.enter_phone("naaaan@mail.ru")
    page.enter_pass("N123456n")
    time.sleep(3)
    page.btn_click()
    time.sleep(3)


def test_auth_page_log(selenium):
    page = AuthPage(selenium)
    page.log_btn_click()
    page.enter_phone("rtkid_1714408787974")
    page.enter_pass("N123456n")
    time.sleep(3)
    page.btn_click()
    time.sleep(3)


def test_forgot_pass(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    forgot_pass = selenium.find_element(*AuthLocators.AUTH_FORGOT_PASS)
    forgot_pass.click()
    page.enter_phone("89112642210")
    time.sleep(20)
    #вводим капчу вручную
    continue_btn = selenium.find_element(*AuthLocators.AUTH_CONTINUE_BTN)
    continue_btn.click()
    time.sleep(10)
    #проверяем, что перешли на страницу ввода кода
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials'


def test_agreement_link(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    agreement_link = selenium.find_element(*AuthLocators.AUTH_AGREEMENT_LINK)
    agreement_link.click()
    time.sleep(5)
    #проверяем, что перешл на страницу "пользовательское соглашение"
    assert page.get_relative_link() == '/auth/realms/b2c/protocol/openid-connect/auth'


def test_help_link(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    help_link = selenium.find_element(*AuthLocators.AUTH_HELP_LINK)
    help_link.click()
    time.sleep(5)
    #проверяем, что перешл на страницу "Помощь"
    assert page.get_relative_link() == '/auth/realms/b2c/protocol/openid-connect/auth'


def test_registration(selenium):
    page = AuthPage(selenium)
    time.sleep(5)
    registration_link = selenium.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("Иван")
    page.enter_surname("Иванов")
    page.enter_email_registration("jgjhdfbvbkvbkd@mail.ru")
    page.enter_pass("N123456n")
    page.enter_pass_confirm("N123456n")
    page.registration_button_clic()
    time.sleep(5)
    #проверяем, что перешли на страницу ввода кода
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


def test_registration_name_empty(selenium):
    page = AuthPage(selenium)
    registration_link = selenium.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name(" ")
    page.enter_surname("Иванов")
    page.enter_email_registration("jgjhdfbvbkvbkd@mail.ru")
    page.enter_pass("N123456n")
    page.enter_pass_confirm("N123456n")
    page.registration_button_clic()
    time.sleep(5)

    error_messages = selenium.find_elements(*AuthLocators.AUTH_ERROR_MESSAGE)
    assert any(error_message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов." for error_message in
               error_messages), "Сообщение об ошибке не найдено на странице регистрации"

def test_registration_name_digit(selenium):
    page = AuthPage(selenium)
    registration_link = selenium.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("111")
    page.enter_surname("Иванов")
    page.enter_email_registration("jgjhdfbvbkvbkd@mail.ru")
    page.enter_pass("N123456n")
    page.enter_pass_confirm("N123456n")
    page.registration_button_clic()
    time.sleep(5)

    error_messages = selenium.find_elements(*AuthLocators.AUTH_ERROR_MESSAGE)
    assert any(error_message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов." for error_message in
               error_messages), "Сообщение об ошибке не найдено на странице регистрации"


def test_registration_pass_length(selenium):
    page = AuthPage(selenium)
    registration_link = selenium.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("Иван")
    page.enter_surname("Иванов")
    page.enter_email_registration("jgjhdfbvbkvbkd@mail.ru")
    page.enter_pass("Nn")
    page.enter_pass_confirm("Nn")
    page.registration_button_clic()
    time.sleep(5)

    error_messages = selenium.find_elements(*AuthLocators.AUTH_ERROR_MESSAGE)
    assert any(error_message.text == "Длина пароля должна быть не менее 8 символов" for error_message in
               error_messages), "Сообщение об ошибке не найдено на странице регистрации"


def test_registration_pass(selenium):
    page = AuthPage(selenium)
    registration_link = selenium.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("Иван")
    page.enter_surname("Иванов")
    page.enter_email_registration("jgjhdfbvbkvbkd@mail.ru")
    page.enter_pass("n123456n")
    page.enter_pass_confirm("n123456n")
    page.registration_button_clic()
    time.sleep(5)

    error_messages = selenium.find_elements(*AuthLocators.AUTH_ERROR_MESSAGE)
    assert any(error_message.text == "Пароль должен содержать хотя бы одну заглавную букву" for error_message in
               error_messages), "Сообщение об ошибке не найдено на странице регистрации"


def test_registration_pass_match(selenium):
    page = AuthPage(selenium)
    registration_link = selenium.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("Иван")
    page.enter_surname("Иванов")
    page.enter_email_registration("jgjhdfbvbkvbkd@mail.ru")
    page.enter_pass("N123456n")
    page.enter_pass_confirm("Parol123")
    page.registration_button_clic()
    time.sleep(5)

    error_messages = selenium.find_elements(*AuthLocators.ELEMENT_LOCATOR)
    assert any(error_message.text == "Пароли не совпадают" for error_message in
               error_messages), "Сообщение об ошибке не найдено на странице регистрации"

