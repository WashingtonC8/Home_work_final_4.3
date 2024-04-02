from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button_add_to_cart.click()

    def should_be_real_book_name_in_alert(self):
        alert_book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK_ALERT)
        a_b_n = alert_book_name.text
        print(a_b_n)
        real_book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK_REAL)
        r_b_n = real_book_name.text
        print(r_b_n)
        assert a_b_n == r_b_n, "the names of the books in the alert do not match the real one"





