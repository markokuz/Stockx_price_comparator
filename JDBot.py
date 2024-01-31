
from selenium.webdriver.common.keys import Keys
from seleniumbase import BaseCase
import random
BaseCase.main(__name__,__file__, "--uc")

class JDBOT(BaseCase):

    def test_main(self):
        driver1 = self.open("https://stockx.com/")
        driver2 = self.get_new_driver()
        self.get("https://jdsports.ca/collections/mens-shoes-sale?refinementList%5Bvendor%5D%5B0%5D=Nike")

        for i in range(1,10):

            #clicking the shoe from the sale page
            self.switch_to_driver(driver2)
            jd_shoe_Xpath = '//*[@id="algolia-hits"]/div/div['+ str(i) +']/div'
            self.scroll_to(jd_shoe_Xpath)
            self.sleep(random.uniform(1,2))
            self.click(jd_shoe_Xpath)

            productID, JDprice = self.get_info()
            self.get("https://jdsports.ca/collections/mens-shoes-sale?refinementList%5Bvendor%5D%5B0%5D=Nike")
            stockx_price = self.search(productID)
            self.fee_calc(JDprice, stockx_price)

            self.sleep(2)
            self.switch_to_default_driver()


    def fee_calc(self, jdprice, stockxprice):

        #tax
        jdprice_aftertax = float(jdprice)*1.13

        #getting the money made after stockx fees
        stockx_payout = (float(stockxprice)*0.88)-4.48
        profit = stockx_payout-jdprice_aftertax

        if (profit >= 10):
            print(profit)
        else:
            print("not profitable")

        

    #gets the productID (PID) of a shoe from the JD sports website and returns it
    def get_info(self):
        self.sleep(random.uniform(1,3))

        #getting the product price on sale
        price = self.get_text("#ProductSection > div.pdp__details > label > span")
        price = price.replace("Now $", "")

        #getting the shoe product id
        self.click("#trigger-details")
        self.sleep(1)
        PID = self.get_text('//*[@id="info-details"]/p[2]')
        PID = PID.replace("Product Code: ", "")
        return PID, price



    #returns the average sale price of a shoe
    def search(self, PID):
        self.switch_to_default_driver()
        self.type("#site-search", PID)
        element = self.find_element("#site-search")  # Replace '#elementID' with the ID of your target element
        element.send_keys(Keys.ENTER)
        self.sleep(2)

        #clicking the first shoe of the results page
        self.click('//*[@id="browse-grid"]/div/div')
        self.sleep(1)

        #scrolling to the prices grid
        self.scroll_to_bottom()
        self.scroll_to("#main-content > div > section:nth-child(9) > div.css-79elbk > div > div")
        #getting the average price
        price = self.get_text('#main-content > div > section:nth-child(9) > div.css-79elbk > div > div > div:nth-child(6) > dl > dd')
        price = price.replace("CA$", "")
        return price

