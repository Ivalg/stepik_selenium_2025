import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import faker
fake = faker.Faker()


@pytest.mark.user
class TestUserAddToBasketFormProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        self.login_page = LoginPage(self.driver, self.link)
        self.login_page.open()
        self.email = fake.email()
        self.password = fake.password()
        self.login_page.register_new_user(self.email, self.password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(driver, product_link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, driver):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(driver, product_link)
        page.open()
        book_title = page.get_book_title()
        book_price = page.get_book_price()
        page.add_to_basket()
        # page.solve_quiz_and_get_code()
        success_message = page.get_success_message()
        basket_sum = page.get_basket_sum()

        assert book_title == success_message.text
        assert book_price == basket_sum.text


@pytest.mark.skip
@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail(reason="Oшибка в названии '...book'")),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(driver, link):
    product_link = link
    page = ProductPage(driver, product_link)
    page.open()
    book_title = page.get_book_title()
    book_price = page.get_book_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    success_message = page.get_success_message()
    basket_sum = page.get_basket_sum()

    assert book_title == success_message.text
    assert book_price == basket_sum.text


@pytest.mark.xfail(reason="сообщение появляется")
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, product_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, product_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="сообщение не пропадает")
def test_message_disappeared_after_adding_product_to_basket(driver):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, product_link)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)


def test_guest_should_see_basket_url(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket_page()
    login_page = BasketPage(driver, driver.current_url)
    login_page.should_be_basket_url()


def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, product_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_empty_basket_test()
