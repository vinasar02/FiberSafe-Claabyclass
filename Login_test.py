import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from path import path

class Login_Page:

    def __init__(self, driver):
        self.driver = driver

############################## LOGIN ############################################################

#set the username
    def setusername(self,username):
        self.driver.find_element_by_id(path.Login.textbox_username_id).clear()
        self.driver.find_element_by_id(path.Login.textbox_username_id).send_keys(username)

#set the password
    def setpassword(self, password):
        self.driver.find_element_by_id(path.Login.textbox_password_id).clear()
        self.driver.find_element_by_id(path.Login.textbox_password_id).send_keys(password)

#click the login button
    def clicklogin(self):
        self.driver.find_element_by_xpath(path.Login.button_login_xpath).click()