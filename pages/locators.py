from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


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


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    BOOK_TITLE = (By.XPATH, '//h1')
    BOOK_PRICE = (By.XPATH, '//p[@class="price_color"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "alert-success")]//strong')
    BASKET_SUM_MESSAGE = (By.XPATH, '//div[3]/div/p[1]/strong')


class BasketPageLocators:
    TEXT_IN_BASKET = (By.XPATH, '//*[@id="content_inner"]/p')
    PRODUCT_IN_BASKET_TEXT = (By.XPATH, '//h2[@class="col-sm-6 h3"]')
