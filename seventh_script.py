import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'some_text.txt')
    browser = webdriver.Firefox()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '[name = "firstname"]').send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, '[name = "lastname"]').send_keys("Иванов")
    browser.find_element(By.CSS_SELECTOR, '[name = "email"]').send_keys("ivan@mail.ru")
    browser.find_element(By.CSS_SELECTOR, '[id = "file"]').send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(30) #Explicit wait to copy the value from the modal.
    browser.quit()
