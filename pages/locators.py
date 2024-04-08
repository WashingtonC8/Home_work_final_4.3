from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_BOOK_ALERT = (By.CSS_SELECTOR, "div .alertinner strong")
    NAME_BOOK_REAL = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    BOOK_ALERT = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")
    PRICE_ALERT = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in")
    PRICE_BOOK_ALERT = (By.CSS_SELECTOR, "div .alertinner p strong")
    PRICE_BOOK_REAL = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.LINK_TEXT, "Посмотреть корзину")


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    REGISTER_PASSWORD_INPUT_REPEAT = (By.ID, "id_registration-password2")
    REGISTER_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")