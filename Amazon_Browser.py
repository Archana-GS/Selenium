# Learn to navigate to Amazon web page and select a product under different catagory

# Steps :

    # Launching Chrome Driver
    # Navigate to Amazon web page
    # Locate the path of text fields using id and without id
    # Select phones --- click prime check box--- select one plus bluetooth earphones
    # close the browser

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize webdriver
driver = webdriver.Chrome()

# Open URL and maximize window
driver.get("https://www.amazon.in/")
driver.maximize_window()

# Phones button
phones = driver.find_element(by=By.XPATH,value ="//a[contains(text(),'Mobiles')]")
phones.click()

# Prime checkbox 
Prime = driver.find_element(by=By.XPATH,value ="//*[@id='s-refinements']/div[3]/ul/li/span/a/div/label/i")
Prime.click()

# Selecting onepluse bluetooth earphones
oneplus = driver.find_element(by=By.XPATH,value ="//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[3]/div[2]/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/a[1]/div[1]/img[1]")
oneplus.click()
time.sleep(3)
driver.quit()

