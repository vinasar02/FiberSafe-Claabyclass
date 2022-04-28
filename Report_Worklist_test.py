import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from path import path

class Report_Worklist_Page:
    def __init__(self, driver):
        self.driver = driver

################################ REPORT #############################################
# expand the bar
    def reports(self):
        self.driver.find_element_by_xpath(path.Report.expand).click()

# view the worklist
    def worklist(self):
        self.driver.find_element_by_xpath(path.Report.clickoption).click()
        #time.sleep(15)

# ///////////////////////////////////////////////////// STATUS : UPCOMING //////////////////////////////////////////////////////////////////////#
# enter the status "UPCOMING" at the search box
    def searchstatusupcoming(self):
        self.driver.find_element_by_xpath(path.Report.search1).send_keys("Upcoming")
        time.sleep(5)
# click the search button
        self.driver.find_element_by_xpath(path.Report.clicksearch).click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# back to the list of the worklist
        self.driver.find_element_by_xpath(path.Report.backbutton).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.search1).clear()

# ///////////////////////////////////////////////////// STATUS : IN PROGRESS //////////////////////////////////////////////////////////////////////#
# enter the status "IN PROGRESS" at the search box
    def searchstatusinprogress(self):
        self.driver.find_element_by_xpath(path.Report.search1).send_keys("In progress")
        time.sleep(5)
# click the search button
        self.driver.find_element_by_xpath(path.Report.clicksearch).click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
# edit the field team member
    def selectfieldteammember1(self):
        self.driver.find_element_by_xpath(path.Report.edit).click()
        time.sleep(5)
#select any of the field team member name
        select1 = Select(self.driver.find_element_by_id("assignee_upd"))
        select1.select_by_visible_text("Wut Hmone Hnin Hlaing")
        time.sleep(5)
# enter the remark for the field team member
        self.driver.find_element_by_xpath(path.Report.remark).send_keys("Test")
        time.sleep(3)
# click "x" button
        self.driver.find_element_by_xpath(path.Report.clickcancel).click()
# set the date of visit
    def test_calendar_control_range1(self):
        self.driver.find_element_by_xpath(path.Report.frame).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.year).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.month).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.day).click()
        time.sleep(5)
# save the changes
        self.driver.find_element_by_xpath(path.Report.save).click()
        time.sleep(5)
# back to the list of the worklist
        self.driver.find_element_by_xpath(path.Report.backbutton).click()
# update the status of inspection
    def updatestatus(self):
# choose any of the user from the list
        i = random.randint(1,10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr['+str(i)+']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# click the see details button
        self.driver.find_element_by_xpath(path.Report.seedetails).click()
        time.sleep(5)
# change the inspection status by clicking the edit button
        self.driver.find_element_by_xpath(path.Report.inspection_status).click()
        time.sleep(5)
        Select(self.driver.find_element_by_id("status_upd")).select_by_visible_text("Completed")
        time.sleep(5)
# enter the remark for the status updated
        self.driver.find_element_by_xpath(path.Report.remark1).send_keys("Complete")
#is there any fibercut
    def fibercut(self):
# is therere any fibercut by clicking the edit button
        self.driver.find_element_by_xpath(path.Report.editclick).click()
        time.sleep(5)
#click the box if yes
        self.driver.find_element_by_xpath(path.Report.clickbox).click()
        time.sleep(5)
# enter the remark for the status updated
        self.driver.find_element_by_xpath(path.Report.remark2).send_keys("Cable")
        time.sleep(5)
# click the submit button
        self.driver.find_element_by_xpath(path.Report.submit).click()
        time.sleep(5)
# back to the inspection
        self.driver.find_element_by_xpath(path.Report.backbutton).click()
        time.sleep(3)
# back to the list of the worklist
        self.driver.find_element_by_xpath(path.Report.backbutton).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.search1).clear()

#///////////////////////////////////////////////////// STATUS : SUBMITTED //////////////////////////////////////////////////////////////////////#
# enter the status "SUBMITTED" at the search box
    def searchstatussubmitted(self):
        self.driver.find_element_by_xpath(path.Report.search1).send_keys("Submitted")
        time.sleep(5)
# click the search button
        self.driver.find_element_by_xpath(path.Report.clicksearch).click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# click the see details button
        self.driver.find_element_by_xpath(path.Report.seedetails).click()
# scroll down to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
# edit the revisit
        self.driver.find_element_by_xpath(path.Report.editrevisit).click()
        time.sleep(5)
# click the require revisit
        self.driver.find_element_by_xpath(path.Report.require).click()
        time.sleep(5)

#set the date of visit
    def test_calendar_control_range2(self):
        self.driver.find_element_by_xpath(path.Report.frame1).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.year1).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.month1).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.day1).click()
        time.sleep(5)
#click the submit button
        self.driver.find_element_by_xpath(path.Report.submit1).click()
        time.sleep(5)
# back to the inspection
        self.driver.find_element_by_xpath(path.Report.backbutton).click()
        time.sleep(3)
# back to the list of the worklist
        self.driver.find_element_by_xpath(path.Report.backbutton).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(path.Report.search1).clear()

# ///////////////////////////////////////////////////// STATUS : DECLINE//////////////////////////////////////////////////////////////////////#
# enter the status "DECLINE" at the search box
    def searchstatusdecline(self):
        self.driver.find_element_by_xpath(path.Report.search1).send_keys("Decline")
        time.sleep(5)
# click the search button
        self.driver.find_element_by_xpath(path.Report.clicksearch).click()
        time.sleep(5)
# choose any of the user from the list
        self.driver.find_element_by_xpath(path.Report.choice).click()
# edit the field team member
    def selectfieldteammember3(self):
        self.driver.find_element_by_xpath(path.Report.edit).click()
        time.sleep(5)
# select any of the field team member name
        select1 = Select(self.driver.find_element_by_id("assignee_upd"))
        select1.select_by_visible_text("arfan FT 2")
        time.sleep(5)
# enter the remark for the field team member
        self.driver.find_element_by_xpath(path.Report.remark).send_keys("Test")
        time.sleep(5)

#set the date of visit
    def test_calendar_control_range3(self):
        self.driver.find_element_by_xpath(path.Report.frame).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.year).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.month).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.day).click()
        time.sleep(5)
# save the changes
        self.driver.find_element_by_xpath(path.Report.save).click()
        time.sleep(5)
# back to the list of the worklist
        self.driver.find_element_by_xpath(path.Report.backbutton).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.search1).clear()

# ///////////////////////////////////////////////////// STATUS : INVALID //////////////////////////////////////////////////////////////////////#
# enter the status "INVALID" at the search box
    def searchstatusinvalid(self):
        self.driver.find_element_by_xpath(path.Report.search1).send_keys("Invalid")
        time.sleep(5)
# click the search button
        self.driver.find_element_by_xpath(path.Report.clicksearch).click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# back to the list of the worklist
        self.driver.find_element_by_xpath(path.Report.backbutton).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(path.Report.search1).clear()
        time.sleep(10)


