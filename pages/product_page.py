from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button_add_to_cart.click()

    def should_be_name_book_alert(self):
        assert self.is_element_present(*ProductPageLocators.NAME_ALERT), "Alert book name is not presented"

    def should_be_price_book_alert(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_ALERT), "Alert price is not presented"

    def should_be_real_book_name_in_alert(self):
        alert_book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK_ALERT)
        a_b_n = alert_book_name.text
        print(a_b_n)
        real_book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK_REAL)
        r_b_n = real_book_name.text
        print(r_b_n)
        assert a_b_n == r_b_n, "the names of the books in the alert do not match the real one"

    def should_be_real_book_price_in_alert(self):
        alert_book_price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_ALERT)
        a_b_p = alert_book_price.text
        print(a_b_p)
        real_book_price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_REAL)
        r_b_p = real_book_price.text
        print(r_b_p)
        assert a_b_p == r_b_p, "the price of the books in the alert do not match the real one"
