import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from path import path

class Map_Page:
    def __init__(self, driver):
        self.driver = driver
################################ MAP #############################################

# click the Map at Menu Bar
    def Map(self):
        self.driver.find_element_by_xpath(path.Map.menubarmap).click()

# enter the address
    def searchaddress(self):
        search = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/input')
        search.send_keys('TM CYBERJAYA TOWER, Cyberjaya, Selangor, Malaysia')
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        #self.driver.find_element_by_xpath(path.Map.search).send_Keys ("TM CYBERJAYA TOWER, Cyberjaya, Selangor, Malaysia")
        #time.sleep(5)
        #search.send_keys(Keys.ENTER)

# choose the cable type
    def cabletype(self):
        self.driver.find_element_by_xpath(path.Map.clickbutton).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Map.clickbutton1).click()