from selenium.webdriver.common.by import By


class TestGoodPage:
    def test_button_add_to_basket(self, browser, language):
        browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
        assert browser.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
