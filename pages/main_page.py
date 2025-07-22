from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):  # переходим на страницу логина
        login_link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # alert = self.driver.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):  # находим кнопку "Войти или зарегистрироваться"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
