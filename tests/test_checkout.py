import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_saucedemo_checkout():
    # Setup driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) # Prevents the "long wait/freeze" issues from earlier
    
    try:
        # 1. Login Flow
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # 2. Add Backpack to Cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
        # 3. Go to Cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # 4. Click Checkout
        driver.find_element(By.ID, "checkout").click()
        
        # 5. Enter Details (Step 16 Customer Data)
        driver.find_element(By.ID, "first-name").send_keys("Pew")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("10000")
        driver.find_element(By.ID, "continue").click()
        
        # 6. Finish Order
        driver.find_element(By.ID, "finish").click()
        
        # 7. Verify Order Success
        assert "Thank you for your order!" in driver.page_source
        print("Test Passed: Checkout completed successfully!")

    finally:
        # Cleanup
        driver.quit()