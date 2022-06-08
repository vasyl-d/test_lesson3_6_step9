from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pytest

wel_mess = "Button text = "
urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]

def op_link(link, browser):
    try:
        browser.get(link)
        time.sleep(30)
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
        )
        mess = ('success', element.text)

    except Exception as ex:
        mess = ('fail', f"An exception of type {type(ex).__name__} occurred.")

    return mess


class TestCartButton():

    @pytest.mark.parametrize('page', urls)
    def test_link(self, browser, page):
        print("start test link: ", page)
        mess = op_link(page, browser)
        assert mess[0] == 'success', mess
