from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("https://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book")))
button.click()

x = browser.find_element(By.ID, "input_value").text
y = str(math.log(abs(12 * math.sin(int(x)))))
browser.find_element(By.CLASS_NAME, "form-control").send_keys(y)
browser.find_element(By.ID, "solve").click()

answer = browser.switch_to.alert.text
print(answer)