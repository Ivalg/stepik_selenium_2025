from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert 'basket' in self.driver.current_url, 'URL does not contain "button"'

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_TEXT), \
            "There are products is the basket, but should not be"

    def should_be_empty_basket_test(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_IN_BASKET), \
            "There should be text that the basket is empty, but it is not"
