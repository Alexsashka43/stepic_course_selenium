import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage:

    @pytest.mark.parametrize('num', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
    def test_guest_should_see_login_link(self, browser, num):
        some_text = ''
        browser.get('https://stepik.org/notifications?auth=login')
        browser.find_element(By.CSS_SELECTOR, '[name = "login"]').send_keys('qwertypitec@gmail.com')
        browser.find_element(By.CSS_SELECTOR, '[name = "password"]').send_keys('461121steP.')
        browser.find_element(By.CSS_SELECTOR, '[class="sign-form__btn button_with-loader "]').click()
        time.sleep(3)
        browser.get(f'https://stepik.org/lesson/{num}/step/1')
        answer = math.log(int(time.time()))
        browser.find_element(By.TAG_NAME, "textarea").send_keys(answer)
        browser.find_element(By.CSS_SELECTOR, '[class="submit-submission"]').click()
        text = browser.find_element(By.CSS_SELECTOR, '[class ="smart-hints__hint"]').text
        assert text == 'Correct!', f'{some_text.join(text)}'
