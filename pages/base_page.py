from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage():
    # конструктор-метод, в качетсве параметров передаются: экземпляр драйвера, url адрес, неявное ожидание
    def __init__(self, browser, url, timeout=10):
        # внутри конструктора данные сохраняются как атрибуты класса
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # метод открытия нужной страницы в браузере
    def open(self):
        self.browser.get(self.url)

    # метод поиска элемента, в котором перехватываются исключения
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # метод для получения проверочного кода
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # метод, который проверяет, что какой-то элемент исчезает
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # метод для проверки ссылки на логин
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

   # метод перехода на страницу логина
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # метод перехода в корзину с помощью нажатия по кнопке в шапке сайта
    def go_to_basket(self):
        button = self.browser.find_element(*BasePageLocators.BUTTON_ADD)
        button.click()

    # метод проверяет, что пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"
