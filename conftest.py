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
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield driver
    driver.quit()
    print('\nquit browser..')
