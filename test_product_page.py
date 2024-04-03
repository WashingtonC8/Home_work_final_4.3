from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_name_book_alert()
    page.should_be_real_book_name_in_alert()
    page.should_be_price_book_alert()
    page.should_be_real_book_price_in_alert()
