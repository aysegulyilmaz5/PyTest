import pytest
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

class TestLogin:
    def test_login_chrome(self):
        serv_obj = ChromeService("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
        driver = ChromeWebDriver(service=serv_obj)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.NAME, "Submit").click()
        assert driver.title == "OrangeHRM"
        driver.quit()

    def test_login_edge(self):
        serv_obj = EdgeService("C:\\Drivers\\edgedriver_win32\\msedgedriver.exe")
        driver = EdgeWebDriver(service=serv_obj)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.NAME, "Submit").click()
        assert driver.title == "OrangeHRM"
        driver.quit()

    def test_login_firefox(self):
        serv_obj = FirefoxService("C:\\Drivers\\geckodriver_win32\\geckodriver.exe")
        driver = FirefoxWebDriver(service=serv_obj)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.NAME, "Submit").click()
        assert driver.title == "OrangeHRM"
        driver.quit()