import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:

#Add Locators for every elements on the page.
    buttonCustomers_menu_xpath = '//a[@href= "#"] //p[contains(text(), "Customers")]'
    buttonCustomers_sub_menu_xpath = '//a[@href= "/Admin/Customer/List"] //p[contains(text(), "Customers")]'
    buttonAddNew_xpath = '//*[@class = "btn btn-primary"]'

    txtEmail_xpath = '//input[@id= "Email"]'
    txtPassword_xpath = '//input[@id= "Password"]'
    txtFirstName_xpath = '//input[@id= "FirstName"]'
    txtLastName_xpath = '//input[@id= "LastName"]'
    rb_GenderMale_xpath = '//input[@id= "Gender_Male"]'
    rb_GenderFemale_xpath = '//input[@id= "Gender_Female"]'
    txtDateOfBirth_xpath = '//input[@id= "DateOfBirth"]'
    txtCompanyName_xpath = '//input[@id= "Company"]'
    #txtnewsletter_xpath = ""
    txtCustomerRoles_xpath = '//div[@class = "input-group-append input-group-required"]'
    list_item_Roles_Registered_xpath = '//ul[@role = "listbox"]  //li[(text() = "Registered")]'
    list_item_Roles_ForumModerators_xpath = '//ul[@role = "listbox"]  //li[(text() = "Forum Moderators")]'
    list_item_Roles_Administrators_xpath = '//ul[@role = "listbox"]  //li[(text() = "Administrators")]'
    list_item_Roles_Guests_xpath = '//ul[@role = "listbox"]  //li[(text() = "Guests")]'
    list_item_Roles_Vendor_xpath = '//ul[@role = "listbox"]  //li[(text() = "Vendors")]'
    drop_down_ManagerOfVendor_xpath = '//select[@id= "VendorId"]'
    txtAdminComment_xpath = '//textarea[@id= "AdminComment"]'
    button_Save_xpath = '//button[@name= "save"]'



    def __init__(self,driver):
        self.driver = driver


#Add action methods.
    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.buttonCustomers_menu_xpath).click()

    def clickOnCustomerSubMenu(self):
        self.driver.find_element(By.XPATH, self.buttonCustomers_sub_menu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.buttonAddNew_xpath).click()



    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rb_GenderMale_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rb_GenderFemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rb_GenderMale_xpath).click()

    def setDob(self,dob):
        self.driver.find_element(By.XPATH, self.txtDateOfBirth_xpath).send_keys(dob)

    def setCompanyName(self,compname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(compname)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_Roles_Registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_Roles_Administrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered or Guest, only one is allowed to be.
            self.driver.find_element(By.XPATH, '//span[@title="delete"]').click()
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_Roles_Guests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_Roles_Registered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_Roles_Vendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.list_item_Roles_Guests_xpath)
        time.sleep(1)

        # Теперь нужно кликнуть на listitem.
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH, self.drop_down_ManagerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.button_Save_xpath).click()















