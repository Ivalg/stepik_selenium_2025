from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(driver):
    product_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(driver, product_link)
    page.open()
    book_title = page.get_book_title()
    bool_price = page.get_book_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    success_message = page.get_success_message()
    basket_sum = page.get_basket_sum()

    assert book_title in success_message.text
    assert bool_price in basket_sum.text
