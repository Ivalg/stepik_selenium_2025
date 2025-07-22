import pytest
from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

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
    product_link = link
    page = ProductPage(driver, product_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    product_link = link
    page = ProductPage(driver, product_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="сообщение не пропадает")
def test_message_disappeared_after_adding_product_to_basket(driver):
    product_link = link
    page = ProductPage(driver, product_link)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()
