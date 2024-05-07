from .base_page import BasePage
from .locators import AuthLocators

import time,os

class AuthPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/auth"
        driver.get(url)

    def enter_email(self, value):
        email = self.driver.find_element(*AuthLocators.AUTH_EMAIL)
        email.send_keys(value)

    def enter_pass(self, value):
        password = self.driver.find_element(*AuthLocators.AUTH_PASS)
        password.send_keys(value)

    def btn_click(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_BTN)
        btn.click()

    def email_btn_click(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_EMAIL_BTN)
        btn.click()

    def log_btn_click(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_LOG_BTN)
        btn.click()

    def enter_phone(self, value):
        phone = self.driver.find_element(*AuthLocators.AUTH_PHONE)
        phone.send_keys(value)

    def open_auth_page(self):
        self.open_page(self.url)

    def enter_name(self, value):
        name = self.driver.find_element(*AuthLocators.AUTH_NAME_REGISTRATION)
        name.send_keys(value)

    def enter_surname(self, value):
        surname = self.driver.find_element(*AuthLocators.AUTH_SURNAME_REGISTRATION)
        surname.send_keys(value)

    def enter_email_registration(self, value):
        email = self.driver.find_element(*AuthLocators.AUTH_EMAIL_REGISTRATION)
        email.send_keys(value)

    def enter_pass_confirm(self, value):
        pass_confirm = self.driver.find_element(*AuthLocators.AUTH_PASS_CONFIRM)
        pass_confirm.send_keys(value)

    def registration_button_clic(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_REGISTRATION_BTN)
        btn.click()

    def forgot_pass_click(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_FORGOT_PASS)
        btn.click()

    def continue_btn(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_CONTINUE_BTN)
        btn.click()




