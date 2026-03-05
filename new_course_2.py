from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

'''
link = "https://suninjuly.github.io/registration2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[3]/input")
    input3.send_keys("bbbb@vvv.b")
    input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[1]/input")
    input3.send_keys("457665867")
    input4 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input")
    input4.send_keys("Rossosissia")
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    answer = browser.switch_to.alert.text
    print(answer)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''

'''
link = "https://suninjuly.github.io/math.html"
try:
    def calc(number):
        return str(math.log(abs(12 * math.sin(int(number)))))
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()

    answer = browser.switch_to.alert.text
    print(answer)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''


link = "https://suninjuly.github.io/get_attribute.html"
try:
    def calc(number):
        return str(math.log(abs(12 * math.sin(int(number)))))
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.TAG_NAME, "img").get_attribute("valuex")
    y = calc(int(x))
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()

    answer = browser.switch_to.alert.text
    print(answer)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
