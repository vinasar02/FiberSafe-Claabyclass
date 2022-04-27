import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from path import path

class Dashboard_Page:
    def __init__(self, driver):
        self.driver = driver

############################## DASHBOARD ############################################################

#click decline card and click dashboard back
    def clickcard(self):
        self.driver.find_element_by_xpath(path.Dashboard.dashbutton).click()
        time.sleep(10)
        self.driver.find_element_by_xpath(path.Dashboard.back).click()


#click the dropdown button and choose FiberCut to look the bar
    def selectbar(self):
        select = Select(self.driver.find_element_by_id("chart_type"))
        select.select_by_visible_text("Fiber Cut")

 #scroll down to the bottom of the page
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# click the dropdown button and choose unmatched to look the number of data
    def reportsource(self):
        select = Select(self.driver.find_element_by_id("source_type"))
        select.select_by_visible_text("Unmatched")

# click any data to look on the recent worklist
    def recentworklist(self):
        self.driver.find_element_by_xpath(path.Dashboard.pressalert).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Dashboard.backbutton).click()
