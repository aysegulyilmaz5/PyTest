import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser== "chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("C:\\Driver\\chromedriver_win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    return driver
def pytest_addoption(parser): #This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will rturn the Browser value to setup method
    return request.config.getoption("--browser")
# #customizing HTML report
# #It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name']='Orange HRM'
#     config._metdata['Module Name']='Login Module'
#     config._metdata['Tester Name']='Aysegul'

# #It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Python",None)
#     metadata.pop("Plugins",None)