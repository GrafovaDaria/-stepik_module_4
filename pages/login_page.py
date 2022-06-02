from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # метод проверки на корректный url адрес
    def should_be_login_url(self, current_url=None):
        assert "login" in current_url, "There is no 'login' in the url"

    # метод проверки, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_ADDRESS), "Login address is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"

    # метод проверки, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_ADDRESS), "Register address is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_1), "Register password1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_2), "Register password2  is not presented"

    # метод для регистрации пользователя
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_ADDRESS)
        email_input.send_keys(email)
        password_1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        password_1.send_keys(password)
        password_2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        password_2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()