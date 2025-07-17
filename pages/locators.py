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


class ProductPageLocator:
    ADD_BASKET_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    BOOK_TITLE = (By.XPATH, '//h1')
    BOOK_PRICE = (By.XPATH, '//p[@class="price_color"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "alert-success") and contains(., "добавлен в вашу корзину")]')
    BASKET_SUM = (By.XPATH, '//div[contains(@class, "alert-info") and contains(., "Стоимость корзины")]')