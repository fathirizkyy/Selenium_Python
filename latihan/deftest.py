from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
