from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.TAG_NAME, "button").click()
    alert = browser.switch_to.alert.accept()


finally:
    time.sleep(30) #Explicit wait to copy the value from the modal.
    browser.quit()
