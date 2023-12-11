import logging

from .loginPage import TestLogin
from .deftest import setup
import pytest

#logging.basicConfig(filename='test_log.txt', level=logging.ERROR)
@pytest.mark.usefixtures("setup")
class TestMulai:
    def test_success(self, setup):
        test_login = TestLogin(setup)
        try:
            test_login.open()
            test_login.login("standard_user", "secret_sauce")
            text = test_login.get_sukses().text
            assert text in "Products"
        except Exception as ex:
            logging.error(f"{ex}")
            test_login.screenshots("test_login_sukses")
            raise
        finally:
            #setup.save_screenshot("assertion_failure.png")
            test_login.quit()

    def test_invalid_username(self,setup):
        test_login = TestLogin(setup)
        try:
            test_login.open()
            test_login.login("standard_user", "secret_sauce")
            text = test_login.get_gagal().text
            assert text in "Epic sadface: Username and password do not match any user in this service"
        except Exception as ex:
            logging.error(f"{ex}")
            test_login.screenshots("test_invalid_username")
            raise
        finally:
            test_login.quit()

    def test_invalid_password(self,setup):
        test_login = TestLogin(setup)
        try:
            test_login.open()
            test_login.login("standard_user", "secret")
            text = test_login.get_gagal().text
            assert text in "Epic sadface: Username and password do not match any user in this service"
        except Exception as ex:
            logging.error(f"{ex}")
            test_login.screenshots("test_invalid_password")
            raise
        finally:
            test_login.quit()

    def test_without_username(self,setup):
        test_login=TestLogin(setup)
        try:
            test_login.open()
            test_login.login_password("secret_sauce")
            text = test_login.get_gagal().text
            assert text in "Epic sadface: Username is required"
        except Exception as ex:
            logging.error(f"{ex}")
            test_login.screenshots("test_without_username")
            raise
        finally:
            test_login.quit()
