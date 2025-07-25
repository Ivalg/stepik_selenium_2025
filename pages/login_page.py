from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        # self.should_be_correct_forgot_password_link()

    def should_be_login_url(self):
        assert 'login' in self.driver.current_url, 'URL does not contain "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_FIELD), 'Login field is not visible'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), 'Password field is not visible'
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_BUTTON), 'Login button is not visible'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FIELD), 'Email field is not visible'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD), 'Password field is not visible'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_FIELD), \
            'Confirm password field id not visible'
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_BUTTON), \
            'Register button is not visible'

    def register_new_user(self, email, password):
        reg_email_field = self.driver.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        reg_email_field.send_keys(email)
        reg_pass_field = self.driver.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        reg_pass_field.send_keys(password)
        reg_pass_conf_field = self.driver.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_FIELD)
        reg_pass_conf_field.send_keys(password)
        reg_button = self.driver.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
        reg_button.click()