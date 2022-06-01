import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    #по умолчанию язык - ru
    parser.addoption('--language', action='store', default='ru', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': request.config.getoption('language')})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()