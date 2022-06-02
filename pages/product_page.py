from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators


class ProductPage(BasePage):

    def should_be_element_page(self):
        self.should_be_name_product()
        self.should_be_price_product()
        self.should_be_add_button()

    #  метод проверки наличия названия товара
    def should_be_name_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Name product is not presented"

    # метод проверки наличия цены товара
    def should_be_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Price product is not presented"

    # метод, который вытаскивает из элемента текст-название товара
    def return_product_name(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text

    # метод, который вытаскивает из элемента текс-цена товара
    def return_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text

    # метод проверки наличия кнопки "Добавить в корзину"
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Button add is not presented"

    #метод добавления в корзину с проверкой на совпадение имен добавляемого товара и добавленного
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()
        #self.solve_quiz_and_get_code()
        assert self.return_product_name() == self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "The names of the products do not match"

    # метод проверки появления успешного сообщения о добавлении товара
    def should_be_product_added_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "There is no message about the successful addition"

    # метод проверяет, что не должно быть сообщения о добавлении товара
    def should_be_no_success_message_with_add(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    # метод проверяет, что не должно быть сообщения о добавлении товара
    def should_be_no_success_message_without_add(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    # метод проверяет, что не должно быть сообщения о добавлении товара
    def should_be_no_success_message_with_disappeared(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    # метод перехода на страницу входа
    def go_to_login_page_from_product_page(self):
        login = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login.click()