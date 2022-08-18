# """
# Learn to navigate to Weathershopper web page using selenium

#Steps :

    # Launching Chrome Driver
    # Navigate to Weathershopper page
    # Perform click action on Moisturizer or sunscreens based on temperature
    # Select a least priced product and add to cart
    # Click on pay with card
    # Close the browser


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# launching the driver
driver=webdriver.Chrome()
# Maximizing the window
driver.maximize_window()

# driver.get method is navigate to the page of given URL
driver.get("https://weathershopper.pythonanywhere.com/")
# Print the title of page
# print(driver.title)
# print(driver.current_url)

# Locate the button and perform click action
temp_txt=driver.find_element(by=By.XPATH,value ="//span[@id='temperature']")
temp_txt.text

# Perform click action on Moisturizer if temperature is less than 20°C
if  (temp_txt.text) <= ('20°C') :
    time.sleep(2)
    button=driver.find_element(by=By.XPATH,value = "//button[contains(text(),'Buy moisturizers')]").click()
    elems = driver.find_elements(by=By.XPATH,value ="//p[contains(text(),'Price')]")
    price_list = []
    least_priced_item = 1000

# Select least priced product
    for elem in elems:
        print(elem)
        elem_txt=int((elem.text)[-3::])
        price_list.append(elem_txt)
    print(price_list)
    mini = min(price_list)
    print(mini)
    
    # if mini < least_priced_item:
    #     least_priced_item=str(mini)
    least_item_text = elem.find_element(by=By.XPATH,value ="//p[contains(text(),'"+mini+"')]/following-sibling::button[@class='btn btn-primary']").click()

# Perform click action on Sunscreens if temperature is more than 30°C        
elif (temp_txt.text) >= ('30°C') :
    time.sleep(2)
    button=driver.find_element(by=By.XPATH,value = "//button[contains(text(),'Buy sunscreens')]").click()
    elems = driver.find_elements(by=By.XPATH,value ="//p[contains(text(),'Price')]")
    price_list = []
    least_priced_item = 1000

# Select least priced product    
    for elem in elems:
        print(elem)
        elem_txt=int((elem.text)[-3::])
        price_list.append(elem_txt)
    print(price_list)
    mini = min(price_list)
    print(mini)

    # if mini < least_priced_item:
    #     least_priced_item=str(mini)
    least_item_text = elem.find_element(by=By.XPATH,value ="//p[contains(text(),'"+mini+"')]/following-sibling::button[@class='btn btn-primary']").click()

# Click cart button
button=driver.find_element(by=By.XPATH,value ="//button[@class='thin-text nav-link']").click()
# Pause the page for 2 seconds
time.sleep(2)
# Click pay with card button
button=driver.find_element(by=By.XPATH,value ="//span[normalize-space()='Pay with Card']").click()
# Pause the page for 3 seconds
time.sleep(3)
# Close the browser
driver.close()