from selenium import webdriver

# 1. Test Successful Login + Add Product to Cart
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    # Log in
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # Verify we are logged in
    assert "inventory" in driver.current_url

    # Add a product to the cart
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()

    driver.quit()

# 2. Test Invalid Login
def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    # Try invalid credentials
    driver.find_element("id", "user-name").send_keys("wrong")
    driver.find_element("id", "password").send_keys("wrong")
    driver.find_element("id", "login-button").click()

    # Capture and verify the error message
    error = driver.find_element("css selector", "h3").text
    assert "Epic sadface" in error

    # Close the browser 
    driver.quit()

def test_login2():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    # 1. Log in
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # 2. Click Add to Cart
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()

    # --- VERIFICATION METHOD A: Check the Shopping Cart Badge ---
    # Find the shopping cart badge element and grab its text content
    cart_badge_text = driver.find_element("css selector", ".shopping_cart_badge").text
    # Assert that the cart now contains exactly "1" item
    assert cart_badge_text == "1"

    # --- VERIFICATION METHOD B: Check Button Text Change ---
    # Find the button again (its ID changes to 'remove-...' after clicking)
    button_text = driver.find_element("id", "remove-sauce-labs-backpack").text
    # Assert that the button text switched to "Remove"
    assert button_text == "Remove"

    driver.quit()