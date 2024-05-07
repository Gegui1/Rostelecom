from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    AUTH_EMAIL_BTN = (By.ID, "t-btn-tab-mail")
    AUTH_LOG_BTN = (By.ID, "t-btn-tab-login")
    AUTH_PHONE = (By.ID, "username")
    AUTH_REGISTRATION_LINK = (By.ID, "kc-register")
    AUTH_NAME_REGISTRATION = (By.NAME, "firstName")
    AUTH_SURNAME_REGISTRATION = (By.NAME, "lastName")
    AUTH_EMAIL_REGISTRATION = (By.ID, "address")
    AUTH_PASS_CONFIRM = (By.ID, "password-confirm")
    AUTH_REGISTRATION_BTN = (By.CSS_SELECTOR, 'button[name="register"]')
    AUTH_FORGOT_PASS = (By.ID, "forgot_password")
    AUTH_CONTINUE_BTN = (By.ID, "reset")
    AUTH_HELP_LINK = (By.ID, "faq-open")
    AUTH_AGREEMENT_LINK = (By.ID, "rt-auth-agreement-link")
    AUTH_ERROR_MESSAGE = (By.CLASS_NAME, 'rt-input-container__meta--error')
    ELEMENT_LOCATOR = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span')






