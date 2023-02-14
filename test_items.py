from time import sleep
from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestPage:

    def test_is_add_to_basket(self, browser):
        browser.get(url)
        #sleep(30)
        btn = browser.find_elements(By.CSS_SELECTOR, '#add_to_basket_form>button')
        assert btn, 'Not found button - "Add to basket"'