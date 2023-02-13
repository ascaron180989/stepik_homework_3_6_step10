# from time import sleep
from selenium.webdriver.common.by import By
from conftest import BASE_PATH

PAGE_PATH = '/catalogue/coders-at-work_207'


class TestPage:

    def test_add_to_basket(self, browser):
        driver, language = browser
        url = BASE_PATH + language + PAGE_PATH
        driver.get(url)
        btn = driver.find_elements(By.CSS_SELECTOR, '#add_to_basket_form>button')
        assert btn, 'Not found button - "Add to basket"'
        # sleep(10)
