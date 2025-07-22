from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url_with_newyear()
        self.add_to_basket()
        self.get_book_title()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is displayed but should disappear"

    def add_to_basket(self):
        add_button = self.driver.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_button.click()

    def get_book_title(self):
        return self.driver.find_element(*ProductPageLocators.BOOK_TITLE).text

    def get_book_price(self):
        return self.driver.find_element(*ProductPageLocators.BOOK_PRICE).text

    def get_success_message(self):
        return self.driver.find_element(*ProductPageLocators.SUCCESS_MESSAGE)

    def get_basket_sum(self):
        return self.driver.find_element(*ProductPageLocators.BASKET_SUM)

    def should_be_product_url_with_newyear(self):
        assert 'newYear' in self.driver.current_url, 'URL does not contain "newYear"'
