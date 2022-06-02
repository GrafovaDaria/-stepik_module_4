from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_ADDRESS = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:first-child .alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-group>:first-child.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ORDER = (By.CSS_SELECTOR, ".btn-block")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")