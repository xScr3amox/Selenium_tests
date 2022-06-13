from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    time.sleep(2)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    _find = browser.find_element(By.XPATH, "//img")
    x = _find.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()

    check1 = browser.find_element(By.CSS_SELECTOR, "div:nth-child(4) #robotsRule")
    check1.click()

    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()

    time.sleep(10)
finally:
    browser.quit()

