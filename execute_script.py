from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

try:
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "div:nth-child(2) .form-check-custom #robotCheckbox").click()

    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(10)
finally:
    browser.quit()