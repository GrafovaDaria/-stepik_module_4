import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function") #фикстура, обрабатывающая переданные в опции данные
def browser(request):
    options = Options() #для указания языка браузера
    options.add_experimental_option('prefs', {'intl.accept_languages': request.config.getoption('language')})
    browser = webdriver.Chrome(options=options)
    yield browser #финализатор
    browser.quit()
