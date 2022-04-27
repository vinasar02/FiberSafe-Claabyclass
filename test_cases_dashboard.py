import time
import unittest
from selenium import webdriver
from pageObjects.Login_test import Login_Page
from pageObjects.Dashboard_test import Dashboard_Page

class Test_Cases_Dashboard(unittest.TestCase):
    exec_path = "C:\\Users\\User\\Documents\\chromedriver.exe"
    base_URL = "https://fibersafe.tmrnd.com.my:86/portal/login"
    username = "PLTest0134"
    password = "Test1234"
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=cls.exec_path)
        cls.driver.get(cls.base_URL)
        cls.driver.maximize_window()
        time.sleep(3)
        # yield
        # self.driver.close()
        # self.driver.quit()


    def test_cases2(self):
        self.lp = Login_Page(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        time.sleep(10)
        self.lp = Dashboard_Page(self.driver)
        self.lp.clickcard()
        time.sleep(5)
        self.lp.selectbar()
        time.sleep(5)
        self.lp.scroll()
        time.sleep(5)
        self.lp.reportsource()
        time.sleep(5)
        self.lp.recentworklist()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

