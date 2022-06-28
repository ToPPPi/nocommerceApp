from selenium.webdriver.common.by import By

class LoginPage:
    # Locators for testcases Login Page.
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    button_logout_linktext = "Logout"

    # Initialize driver
    def __init__(self,driver):
        self.driver=driver

    # Action methods.
    def enterUserName(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogoutButton(self):
        self.driver.find_element(By.LINK_TEXT, self.button_logout_linktext).click()




