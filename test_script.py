import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class RegForm(unittest.TestCase):
    link_positive = "http://suninjuly.github.io/registration1.html"
    link_negative = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    def test_positive(self):
        self.browser.get(self.link_positive)
        self.browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input').send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input').send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input').send_keys("test@test.ru")
        self.browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.second_class > input').send_keys("+7 (900) 000-00-00")
        self.browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.second_class > input').send_keys("Smolensk")
        button = self.browser.find_element(By.TAG_NAME, "button")
        button.click()
        self.assertEqual(self.browser.find_element(By.TAG_NAME, 'h1').text, 'Congratulations! You have successfully registered!')
        self.browser.quit()


    def test_negative(self):
        self.browser.get(self.link_negative)
        self.browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input').send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input').send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input').send_keys("test@test.ru")
        self.browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.second_class > input').send_keys("+7 (900) 000-00-00")
        self.browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.second_class > input').send_keys("Smolensk")
        button = self.browser.find_element(By.TAG_NAME, "button")
        button.click()
        self.assertEqual(self.browser.find_element(By.TAG_NAME, 'h1').text, 'Congratulations! You have successfully registered!')
        self.browser.quit()
