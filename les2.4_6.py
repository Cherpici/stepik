from selenium.webdriver.chrome.webdriver import WebDriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    driver = WebDriver()
    driver.get(link)

    but1 = driver.find_element_by_xpath('//button[@type="submit"]').click()
    new_window = driver.window_handles[1]
    driver.switch_to_window(new_window)
    x = driver.find_element_by_xpath('//span[@id="input_value"]').text
    y = calc(x)
    pole = driver.find_element_by_xpath('//input[@id="answer"]').send_keys(y)
    but2 = driver.find_element_by_xpath('//button[@type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()