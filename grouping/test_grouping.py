import pytest

class TestClass:
    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("This is login by email...")
        assert True == True
    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("This is login by facebook...")
        assert True == True
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is login by twitter...")
        assert True == True
    @pytest.mark.regression
    def test_SignUpByEmail(self):
        print("This is signup by email...")
        assert True == True
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_SignUpFacebook(self):
        print("This is signup by facebook...")
        assert True == True
    @pytest.mark.regression
    def test_SignUpTwitter(self):
        print("This is signup by twitter...")
        assert True == True