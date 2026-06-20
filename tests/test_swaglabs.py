from selenium import webdriver
import time

# 1. Launch a new instance of the Google Chrome browser controlled by automation
driver = webdriver.Chrome()

# 2. Tell the browser to navigate to the specified website URL (Swag Labs login page)
driver.get("https://www.saucedemo.com")

# 3. Pause the script execution for 5 seconds so i can visually verify the page loaded
time.sleep(100)

# 4. Safely close all open browser windows and terminate the automation session
driver.quit()