# Learn to navigate to Facebook web page and enter the Username and password and perform click action using selenium

#Steps :

    # Launching Chrome Driver
    # Navigate to Facebook web page
    # Print the title of page
    # Locate the path of text fields using id and without id
    # Fill emil and password in respective text fields
    # perform click action on login button
    # close the browser

import email
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# launching the driver
driver=webdriver.Chrome()
# Maximizing the window
driver.maximize_window()

# driver.get method is navigate to the page of given URL and print the title of page
driver.get("https://www.facebook.com/login/")
print(driver.title)
print(driver.current_url)

# Locate the email textfield using id
email = driver.find_element(by=By.XPATH,value = "//input[@id='email']")
email.send_keys('gsarchana93@gmail.com')
# Locate the password textfield without id
password = driver.find_element(by=By.XPATH,value ="//input[@placeholder='Password']")
password.send_keys('12345')
# Locate the path and perform click action on login button
button=driver.find_element(by=By.XPATH,value = "//button[contains(text(),'Log In')]")
button.click()

# Pause the page for 5 seconds
time.sleep(5)
# Close the bowser window
driver.close()        