import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from utilities.ReadConfigurations import ReadConfig
from utilities.Logger import LogGenerator
from utilities import Work_With_Excel



# Наверное под этим классом создаются несколько тест кейсов которые будут выполняться на странице.
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationgURL()                 # baseURL = "https://admin-demo.nopcommerce.com/"     #Эти входные данные записаны в "config.ini" file.
    path = "C:/PycharmProjects/nopcommerceApp/TestData/TestData.xlsx"
    logger = LogGenerator.loggenerator()


# # Test_1.
#     def test_CheckHomePageTitle(self,setup):
#         self.driver = setup                                     # self.driver = webdriver.Chrome() - Это можно удалять потому как я передал "setup" в функцию. Смотреть - conftest.py
#         self.logger.info("************** Test_002_DDT_Login **************")
#         self.logger.info("*********** Verifying Home Page **************")
#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#     #Проверка что заголовок совпадает.
#         if act_title == "Your store. Login":
#             self.driver.close()
#             self.logger.info("*********** CheckHomePageTitle is passed **************")
#             assert True  # Пройден.
#         else:
#             self.driver.save_screenshot("C://PycharmProjects//nopcommerceApp//Screenshots//test_CheckHomePageTitle.png")
#             self.driver.close()
#             self.logger.info("*********** CheckHomePageTitle is failed **************")
#             assert False  # Провален.



# Test_2 Проверяю что могу Login.
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.driver = setup                                      # self.driver = webdriver.Chrome() - Это можно удалять потому как я передал "setup" в функцию. Смотреть - conftest.py
        self.driver.maximize_window()
        self.logger.info("*********** Verifying Login DDT Test **************")
        self.driver.get(self.baseURL)

    # Обращаюсь к Work_With_Excel, чтобы получить данные для username and password. !!!
        self.rows = Work_With_Excel.getRowCount(self.path, "TestData")
        print("Number of Rows in an Excel: ", self.rows)

    # Создать лист для testcase.
        list_status = []

        for r in range(2,self.rows+1):
            self.user = Work_With_Excel.readData(self.path,"TestData",r,1)
            self.password = Work_With_Excel.readData(self.path, "TestData", r, 2)
            self.expected_result = Work_With_Excel.readData(self.path, "TestData", r, 3)

    # Обращаюсь к PageObjects LoginPage. !!!
            self.lp = LoginPage(self.driver)
            self.lp.enterUserName(self.user)
            self.lp.enterPassword(self.password)
            self.lp.clickLoginButton()
            time.sleep(5)

            act_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

    # Проверяю логику приложения.
            if act_title == expected_title:
                if self.expected_result == "Pass":
                    self.logger.info("Passed")
                    self.lp.clickLogoutButton()
                    list_status.append("Pass")
                elif self.expected_result == "Fail":
                    self.logger.info("Failed")
                    self.lp.clickLogoutButton()
                    list_status.append("Fail")

            elif act_title != expected_title:
                if self.expected_result == "Pass":
                    self.logger.info("Failed")
                    list_status.append("Fail")
                elif self.expected_result == "Fail":
                    self.logger.info("Passed")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("Login DDT test is passed.")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test is failed.")
            self.driver.close()
            assert False

        self.logger.info("End of Login DDT Test")
        self.logger.info("Completed Test_002_DDT_Login")














    # #Проверяю что заголовок совпадает.
    #     if act_title == "Dashboard / nopCommerce administration":
    #         self.logger.info("*********** Verifying Login Test is passed **************")
    #         self.driver.close()
    #         assert True     #Пройден.
    #     else:
    #         self.driver.save_screenshot("C://PycharmProjects//nopcommerceApp//Screenshots//test_CheckHomePageTitle.png")
    #         self.driver.close()
    #         self.logger.error("*********** Verifying Login Test is failed **************")
    #         assert False    #Провален.






