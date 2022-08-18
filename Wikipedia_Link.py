# Learn to navigate to wikipedia web page and perform click action on link using selenium

#Steps :

    # Launching Chrome Driver
    # Navigate to wikipedia web page
    # Print the title of page
    # Locate the path of text fields using id
    # perform click action on link
    # close the browser

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# launching the driver
driver=webdriver.Chrome()
# Maximizing the window
driver.maximize_window()

# driver.get method is navigate to the page of given URL and print the title of page
driver.get("https://www.wikipedia.org/")
print(driver.title)
print(driver.current_url)

# Locate the path and perform click action on link
link=driver.find_element(by=By.XPATH,value = "//strong[contains(text(),'English')]")
time.sleep(5)
link.click()

# Pause the page for 5 seconds
time.sleep(5)
# Close the bowser window
driver.close()