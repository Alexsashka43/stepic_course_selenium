import math

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    wait_button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[id="price"]'), '100'))
    button_book = browser.find_element(By.CSS_SELECTOR, '[id="book"]').click()
    browser.execute_script('window.moveBy(0, 100)')
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(y)
    button_submit = browser.find_element(By.CSS_SELECTOR, '[id="solve"]').click()
finally:
    time.sleep(10) #Explicit wait to copy the value from the modal.
    browser.quit()


if __name__ == '__main__':
    print("Some text")
