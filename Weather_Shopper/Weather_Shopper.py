# """
# Learn to navigate to Weathershopper web page using selenium

#Steps :

    # Launching Chrome Driver
    # Navigate to Weathershopper page
    # Perform click action on Moisturizer or sunscreens based on temperature
    # Select a least priced product and add to cart
    # Click on pay with card
    # close the browser


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import conf.locators_confi as locators

# launching the driver
driver=webdriver.Chrome()
# Maximizing the window
driver.maximize_window()

# driver.get method is navigate to the page of given URL
driver.get("https://weathershopper.pythonanywhere.com/")
# Print the title of page
print("page title is :",driver.title)
try:
    assert 'Current Temperature' in driver.title
    print("hurrryy!!! page title is correct")
except Exception as e:
    print("oh nooo!!!wrong page title",format(e))

temperature_text = locators.temperature_text
least_priced_product =locators.least_priced_product
moisturizers_button = locators.moisturizers_button
price_of_all_products = locators.price_of_all
sunscreens_button = locators.sunscreens_button
cart_button = locators.cart_button
payment_button = locators.payment_button

temperature_text = driver.find_element(by = By.XPATH,value = temperature_text)
temperature = int((temperature_text.text)[0:2])
print("current temperature is :",temperature,"°C")

# Creating function for least priced product
def get_least_priced_product():
    for item in items:
        print(item)
        item_price = int((item.text)[-3::])
        price_list_all_products.append(item_price)
    print("price list of all the products :",price_list_all_products)
    minimum_price = str(min(price_list_all_products))
    print("minimum price is :",minimum_price,"Rs")
    least_item_text = item.find_element(by = By.XPATH,value = least_priced_product%minimum_price).click()

# Perform click action on Moisturizer if temperature is less than 20°C
if  temperature <= 25 :
    time.sleep(2)
    moisturizers_button = driver.find_element(by = By.XPATH,value = moisturizers_button).click()
    items = driver.find_elements(by = By.XPATH,value = price_of_all_products)
    
# Perform click action on Sunscreens if temperature is more than 30°C        
elif  temperature > 25 :
    time.sleep(2)
    sunscreens_button = driver.find_element(by = By.XPATH,value = sunscreens_button).click()
    items = driver.find_elements(by = By.XPATH,value = price_of_all_products)
    
price_list_all_products = []
maximum_priced_item = 1000
# calling function for least priced product    
get_least_priced_product() 
   
# Click cart button
cart_button = driver.find_element(by = By.XPATH,value = cart_button).click()
# Pause the page for 2 seconds
time.sleep(2)
# Click pay with card button
payment_button = driver.find_element(by = By.XPATH,value = payment_button).click()
# Pause the page for 3 seconds
time.sleep(3)
# Close the browser
driver.close()
