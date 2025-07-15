from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.driver.current_url, 'Login link is not found'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_FIELD), 'Login field is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), 'Password field is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOT_LINK), 'Forgot link is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_BUTTON), 'Login button is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FIELD), 'Email field is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD), 'Password field is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_FIELD), \
            'Confirm password field id not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_BUTTON), \
            'Register button is not presented'
