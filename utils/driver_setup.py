from selenium import webdriver

#Initializes a Chrome driver instance and maximizes the window.
def get_driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    return driver
