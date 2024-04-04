from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_BOOK_ALERT = (By.CSS_SELECTOR, "div .alertinner strong")
    NAME_BOOK_REAL = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    BOOK_ALERT = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")
    PRICE_ALERT = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in")
    PRICE_BOOK_ALERT = (By.CSS_SELECTOR, "div .alertinner p strong")
    PRICE_BOOK_REAL = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")