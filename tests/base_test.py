import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


class BaseTest:

    @pytest.fixture(autouse=True)
    def webdriver(self):
        return WebDriver()

    @pytest.fixture(scope='function', autouse=True)
    def base_setup(self, webdriver):
        # noinspection PyAttributeOutsideInit
        self.webdriver = webdriver
        yield
        self.webdriver.close()
