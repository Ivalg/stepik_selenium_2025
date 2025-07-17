from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_newYear_url()
        self.add_to_basket()
        self.get_book_title()

    def add_to_basket(self):
        add_button = self.driver.find_element(*ProductPageLocator.ADD_BASKET_BUTTON)
        add_button.click()

    def get_book_title(self):
        return self.driver.find_element(*ProductPageLocator.BOOK_TITLE).text

    def get_book_price(self):
        return self.driver.find_element(*ProductPageLocator.BOOK_PRICE).text

    def get_success_message(self):
        return self.driver.find_element(*ProductPageLocator.SUCCESS_MESSAGE)

    def get_basket_sum(self):
        return self.driver.find_element(*ProductPageLocator.BASKET_SUM)

    def should_be_product_url_with_newyear(self):
        assert 'newYear' in self.driver.current_url, 'URL does not contain "newYear"'
