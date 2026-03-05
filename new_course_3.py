from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os

'''
link = "https://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(number):
        return str(math.log(abs(12 * math.sin(int(number)))))
  #  browser.execute_script("alert('Robots at work');")
  #  browser.execute_script('document.title="Script executing";')

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    browser.find_element(By.TAG_NAME, "button").click()

    answer = browser.switch_to.alert.text
    print(answer)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''

# File Loading
link = "https://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    last_name = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    first_name.send_keys("Nadya")
    last_name.send_keys("No")
    email.send_keys("nnn@nn.n")

    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    browser.find_element(By.TAG_NAME, "button").click()

    answer = browser.switch_to.alert.text
    print(answer)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

