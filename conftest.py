import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose browser language, please ("fr", "ru", "en", "es")')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture()
def driver(request):
    print('\nstart browser')
    options = Options()
    user_language = request.config.getoption('language')
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
    print('\nquit browser..')
