import pytest
from selenium import webdriver

# Чтобы не создавать по несколько раз "self.driver = webdriver.Chrome()", он заменяется фикстурой ниже. Удалить "self" в test_Login.py и заменить на setup.
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome(executable_path="C://Program Files (x86)//chromedriver//chromedriver.exe")
#     return driver



# To run a testcase with a particular browser use:
# - pytest -s -v testCases/test_Login.py --browser chrome
# - pytest -s -v testCases/test_Login.py --browser firefox

# To run a testcase parallel use:
# - pytest -s -v -n-=3 testCases/test_Login.py --browser chrome
# - pytest -s -v -n-=3 testCases/test_Login.py --browser firefox

# To create an HTML Report use:
# - pytest -s -v -n-=3 --html=Reports\report.html testCases/test_Login.py --browser chrome




# Чтобы не создавать по несколько раз "self.driver = webdriver.Chrome()", он заменяется фикстурой ниже. Удалить "self" в test_Login.py и заменить на setup.
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C://PycharmProjects//nopcommerceApp//Drivers//chromedriver.exe")
        print("Launching Chrome browser.")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C://Program Files (x86)//chromedriver//geckodriver.exe")
        print("Launching Firefox browser.")
    else:
        driver = webdriver.Chrome(executable_path="C://PycharmProjects//nopcommerceApp//Drivers//chromedriver.exe")
        print("Launching Default browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser (request):
    return request.config.getoption("--browser")



#Pytest HTML Reports.

def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Tester"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)