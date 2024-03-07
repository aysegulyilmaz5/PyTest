import pytest

@pytest.fixture() #decorator
def setup():
        print("Launching browser...") #Execute once before every test method
        print("Open application...")
        yield
        print("Closing browser") # Executes once after every test method