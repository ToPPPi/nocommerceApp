import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from utilities.ReadConfigurations import ReadConfig
from utilities.Logger import LogGenerator



# Наверное под этим классом создаются несколько тест кейсов которые будут выполняться на странице.
class Test_001_Login:
    baseURL = ReadConfig.getApplicationgURL()                 # baseURL = "https://admin-demo.nopcommerce.com/"     #Эти входные данные записаны в "config.ini" file.
    username = ReadConfig.getUsername()                       # username = "admin@yourstore.com"                    #Эти входные данные записаны в "config.ini" file.
    password = ReadConfig.getPassword()                       # password = "admin"                                  #Эти входные данные записаны в "config.ini" file.
    logger = LogGenerator.loggenerator()


# Test_1.
    #Маркеры создаются для того чтобы запускать тест кейсы в группе.
    @pytest.mark.regression
    def test_CheckHomePageTitle(self,setup):
        self.driver = setup                                     # self.driver = webdriver.Chrome() - Это можно удалять потому как я передал "setup" в функцию. Смотреть - conftest.py
        self.logger.info("************** Test_001_Login **************")
        self.logger.info("*********** Verifying Home Page **************")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
    #Проверка что заголовок совпадает.
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("*********** CheckHomePageTitle is passed **************")
            assert True  # Пройден.
        else:
            self.driver.save_screenshot("C://PycharmProjects//nopcommerceApp//Screenshots//test_CheckHomePageTitle.png")
            self.driver.close()
            self.logger.info("*********** CheckHomePageTitle is failed **************")
            assert False  # Провален.



# Test_2 Проверяю что могу Login.
    @pytest.mark.sanity  # Маркеры создаются для того чтобы запускать тест кейсы в группе.
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup                                      # self.driver = webdriver.Chrome() - Это можно удалять потому как я передал "setup" в функцию. Смотреть - conftest.py
        self.logger.info("*********** Verifying Login Test **************")
        self.driver.get(self.baseURL)
    #Обращаюсь к PageObjects LoginPage. !!!
        self.lp=LoginPage(self.driver)
        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        act_title = self.driver.title
    #Проверяю что заголовок совпадает.
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*********** Verifying Login Test is passed **************")
            self.driver.close()
            assert True     #Пройден.
        else:
            self.driver.save_screenshot("C://PycharmProjects//nopcommerceApp//Screenshots//test_CheckHomePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Verifying Login Test is failed **************")
            assert False    #Провален.






