from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os

'''
link = "https://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)

    x = browser.find_element(By.ID, "input_value").text
    y = math.log(abs(12 * math.sin(int(x))))

    browser.find_element(By.TAG_NAME, "input").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()

    answer = browser.switch_to.alert.text
    print(answer)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''

link = "https://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text
    y = math.log(abs(12 * math.sin(int(x))))

    browser.find_element(By.TAG_NAME, "input").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()

    answer = browser.switch_to.alert.text
    print(answer)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()