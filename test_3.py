import pytest

class TestClass:

    @pytest.fixture() #decorator
    def setup(self):
        print("Launching browser...") #Execute once before every test method
        print("Open application...")
        yield
        print("Closing browser") # Executes once after every test method
    def test_Login(self,setup):
        print("this is login test")

    def test_Search(self,setup):
        print("this is search test")

    def test_Advancedsearch(self):
        print("this is advanced search test")