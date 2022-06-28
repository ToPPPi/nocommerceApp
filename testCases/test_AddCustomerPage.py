import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from utilities.ReadConfigurations import ReadConfig
from utilities.Logger import LogGenerator

import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationgURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGenerator.loggenerator()

#Test 1.
    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************** Test_003_AddCustomer **************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.lp = LoginPage(self.driver)
        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()

        self.logger.info("************** Login is successful **************")
        self.logger.info("************** Starting Add Customer Test **************")

        #Обращаюсь к AddCustomer из AddCustomerPage. !!!
        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.clickOnCustomerMenu()
        self.addcustomer.clickOnCustomerSubMenu()
        self.addcustomer.clickOnAddNew()

        #Создаю рандомный gmail.
        self.random_email = random_generator() + "@gmail.com"
        self.addcustomer.setEmail(self.random_email)
        self.addcustomer.setPassword("test123")
        self.addcustomer.setFirstName("First")
        self.addcustomer.setLastName("Last")
        self.addcustomer.setGender("Male")
        self.addcustomer.setDob("01/01/2022")
        self.addcustomer.setCompanyName("Test")
        self.addcustomer.setCustomerRoles("Guests")
        self.addcustomer.setManagerOfVendor("Vendor 2")
        self.addcustomer.setAdminComment("Test")
        self.addcustomer.clickOnSave()
        self.logger.info("************** Finishing Adding Customer Info **************")

        #Validate test case.
        self.message = self.driver.find_element(By.TAG_NAME, "body").text

        if "customer has been added successfully." in self.message:
            assert True == True
            self.logger.info("************** Add Customer Test Passed **************")
        else:
            self.driver.save_screenshot("C://PycharmProjects//nopcommerceApp//Screenshots//test_addCustomer.png")
            self.logger.info("************** Add Customer Test Failed **************")
            assert True == False

        self.driver.close()
        self.logger.info("************** Ending Home Page Title Test **************")




def random_generator(size = 8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range (size))