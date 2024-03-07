import os
from selenium import webdriver

class TestCLI:
    def test_Login(self):
        driver_path = os.path.join(os.getcwd(), "chromedriver.exe")  # Geçerli dizine "chromedriver.exe" ekleniyor
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        try:
            self.status = self.driver.find_element_by_xpath("//h1[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False
