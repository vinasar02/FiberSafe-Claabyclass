import time
import unittest
from selenium import webdriver
from pageObjects.Login_test import Login_Page

class Test_Cases_Login(unittest.TestCase):
    exec_path = "C:\\Users\\User\\Documents\\chromedriver.exe"
    base_URL = "https://fibersafe.tmrnd.com.my:86/portal/login"
    username = "PLTest0134"
    password = "Test1234"
    driver = None


    @classmethod
# pass in a service object driver & initialize webdriver
# open url and maximize window
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=cls.exec_path)
        cls.driver.get(cls.base_URL)
        cls.driver.maximize_window()
        time.sleep(3)
        # yield
        # self.driver.close()
        # self.driver.quit()

    # call each function from the LoginPage class
    def test_cases1(self):
        self.lp = Login_Page(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()