import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_setup import get_driver

#1. Initialize the driver using your utility function

driver = get_driver()

try:

    #2. Navigate to google
    driver.get("https://www.google.com")

    #.3. Wait for a few seconds to observe the browser,verify it loaded successfully
    time.sleep(5)

finally:
    #4. clean up and Close the browser safely
    driver.quit()
