from seleniumbase import SB
from selenium.webdriver.common.keys import Keys
import random

#gets the productID (PID) of a shoe from the JD sports website and returns it
def get_info():
    sb.sleep(random.uniform(1,3))
    sb.click("#trigger-details")
    sb.sleep(1)
    text = sb.get_text('//*[@id="info-details"]/p[2]')
    text = text.replace("Product Code: ", "")
    return text

#returns the average sale price of a shoe
def search(PID):
    sb.switch_to_default_driver()
    sb.type("#site-search", PID)
    element = sb.find_element("#site-search")  # Replace '#elementID' with the ID of your target element
    element.send_keys(Keys.ENTER)
    sb.sleep(1)
    sb.click('//*[@id="browse-grid"]/div/div')
    
    price = sb.get_text('//*[@id="main-content"]/div/section[7]/div[2]/div/div')
    price = price.replace("CA$", "")
    print(price)
    return price


#sb.sleep(random.uniform(1,4))

with SB(uc=True) as sb:

    #Opening the drivers

    driver1 = sb.driver.get("https://stockx.com/")
    driver2 = sb.get_new_driver()
    sb.driver.get("https://jdsports.ca/collections/mens-shoes-sale?refinementList%5Bvendor%5D%5B0%5D=Nike")
    sb.sleep(2)
    #sb.switch_to_default_driver()
    #sb.type("#site-search", "hello")
    #element = sb.find_element("#site-search")  # Replace '#elementID' with the ID of your target element
    #element.send_keys(Keys.ENTER)

    #getting the first products
    #products go from 1 - 24
    #for shoes in range(1,24):
    sb.driver.click('//*[@id="algolia-hits"]/div/div[1]/div')
    product_code = get_info()
    search(product_code)
    
    sb.sleep(random.uniform(1,3))
    

