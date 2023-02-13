import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

BASE_PATH = 'http://selenium1py.pythonanywhere.com/'
language_list = ('ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it',
                 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans')


def get_chrome_driver():
    options = ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    return driver


def get_firefox_driver():
    options = FirefoxOptions()
    options.add_argument('--width=1920')
    options.add_argument('--height=1080')
    driver = webdriver.Firefox(options=options)
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='ru')


def check_language(request):
    lang = request.config.getoption("language")
    if lang in language_list:
        return lang
    else:
        raise pytest.UsageError("--language invalid value")


def check_browse(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = get_chrome_driver()
    elif browser_name == 'firefox':
        driver = get_firefox_driver()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    return driver


@pytest.fixture(scope='function')
def browser(request):
    driver = check_browse(request)
    language = check_language(request)
    yield driver, language
    driver.quit()