from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.TAG_NAME, "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(30) #Explicit wait to copy the value from the modal.
    browser.quit()
