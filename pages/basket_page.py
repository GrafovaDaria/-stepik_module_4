from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # метод проверки, что в корзине нет товаров
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ORDER), "There are orders in the cart, but there should not be"

    # метод проверки, что есть текст о том, что коризна пуста
    def should_be_message_in_basket(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert 'Ваша корзина пуста' in text, 'Basket not text, but should be'