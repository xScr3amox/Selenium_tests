import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

try:
    browser.find_element(By.NAME, "firstname").send_keys("name")
    browser.find_element(By.NAME, "lastname").send_keys("surname")
    browser.find_element(By.NAME, "email").send_keys("email@email.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(10)
finally:
    browser.quit()