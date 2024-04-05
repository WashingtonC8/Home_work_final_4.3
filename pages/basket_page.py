from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_does_not_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Alert price is not presented"

    def should_be_message_contain_basket_is_empty(self):
        empty_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        message = empty_message.text
        print(message)
        assert "Ваша корзина пуста" in message, "Is no text 'Your basket is empty'"
