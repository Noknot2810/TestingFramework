from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from settings import *


class GUITestClient:
    def __init__(self):
        self.driver = None
        match BROWSER_VAR:
            case Browser.Chrome:
                self.run_chrome_driver()
            case Browser.Firefox:
                self.run_firefox_driver()
        self.driver.maximize_window()

    def run_chrome_driver(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)

    def run_firefox_driver(self):
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=service, options=options)

    def stop_driver(self):
        self.driver.quit()

# TODO: change scope maybe (function, class, module, package, session)?
@pytest.fixture(scope="function")
def driver():
    client = GUITestClient()
    yield client.driver
    client.stop_driver()
