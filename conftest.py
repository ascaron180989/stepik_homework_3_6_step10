import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

browser_list = ('chrome', 'firefox')
language_list = ('ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it',
                 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans')


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='ru')


def check_language(request):
    user_language = request.config.getoption("language")
    if user_language in language_list:
        return user_language
    else:
        raise pytest.UsageError("--language invalid value")


def check_browse(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name in browser_list:
        return browser_name
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")


def get_driver(browser, language):
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        options.add_argument('--window-size=1920,1080')
        driver = Chrome(options=options)
        return driver

    if browser == 'firefox':
        options = FirefoxOptions()
        options.set_preference('intl.accept_languages', language)
        driver = Firefox(options=options)
        return driver


@pytest.fixture(scope='function')
def browser(request):
    browser = check_browse(request)
    language = check_language(request)
    driver = get_driver(browser, language)
    yield driver
    driver.quit()
