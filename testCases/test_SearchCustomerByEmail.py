import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from utilities.ReadConfigurations import ReadConfig
from utilities.Logger import LogGenerator

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationgURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGenerator.loggenerator()

#Test 1.
    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************** Test_004_SearchCustomerByEmail **************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.lp = LoginPage(self.driver)
        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()

        self.logger.info("************** Login is successful **************")
        self.logger.info("************** Starting Search Customer By Email **************")

        # Обращаюсь к AddCustomer из AddCustomerPage. !!!
        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.clickOnCustomerMenu()
        self.addcustomer.clickOnCustomerSubMenu()

        self.searchcustomer = SearchCustomer(self.driver)
        self.searchcustomer.setEmail("abcdefg@gmail.com")
        self.searchcustomer.clickOnSearch()
        time.sleep(3)

        status=self.searchcustomer.searchCustomerByEmail("abcdefg@gmail.com")
        assert True == status
        self.logger.info("************** Email is found and present. **************")
        self.logger.info("************** Test Case 004 is Passed. **************")
        self.driver.close()




