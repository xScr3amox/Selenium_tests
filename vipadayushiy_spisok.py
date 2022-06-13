from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")

    time.sleep(1)

    num1 = browser.find_element(By.CSS_SELECTOR, "h2 #num1")
    num11 = int(num1.text)
    num2 = browser.find_element(By.CSS_SELECTOR, "h2 #num2")
    num22 = int(num2.text)

    def reshenie(num11, num22):
        return str(num11+num22)
    input1 = reshenie(num11, num22)
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(input1)

    submit1=browser.find_element(By.CSS_SELECTOR, ".btn-default")
    submit1.click()
    time.sleep(10)
finally:
    browser.quit()
