from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_USERNAME_FIELD = (By.XPATH, '//input[@id="id_login-username"]')
    LOGIN_PASSWORD_FIELD = (By.XPATH, '//input[@id="id_login-password"]')
    LOGIN_FORGOT_LINK = (By.XPATH, '//a[@href="/ru/password-reset/"]')
    LOGIN_FORM_BUTTON = (By.XPATH, '//button[@name="login_submit"]')
    REGISTER_EMAIL_FIELD = (By.XPATH, '//input[@id="id_registration-email"]')
    REGISTER_PASSWORD_FIELD = (By.XPATH, '//input[@id="id_registration-password1"]')
    REGISTER_PASSWORD_CONFIRM_FIELD = (By.XPATH, '//input[@id="id_registration-password2"]')
    REGISTER_FORM_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
