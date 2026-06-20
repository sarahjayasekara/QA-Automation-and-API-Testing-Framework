from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

driver.find_element("id", "user-name").send_keys("standard_user")

driver.find_element("id", "password").send_keys("secret_sauce")

driver.find_element("id", "login-button").click()

time.sleep(5)

driver.quit()