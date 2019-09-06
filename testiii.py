from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
button = browser.find_element_by_tag_name("button").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
num = browser.find_element_by_id("input_value").text
browser.find_element_by_id("answer").send_keys(calc(int(num)))
browser.find_element_by_tag_name("button").click()
