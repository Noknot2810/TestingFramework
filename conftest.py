from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
import pytest
import selenium.webdriver.chrome.webdriver as chrome
import selenium.webdriver.firefox.webdriver as firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from settings import *
import os
from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_exception_interact(node, call, report):
    """
    Overrides the original hook to add a web page screenshot
    into the allure report (and also to save it into
    "error_screenshots" directory if needed)
    """
    web_driver = None
    for fixture_name in node.fixturenames:
        web_driver = node.funcargs[fixture_name]
        if (isinstance(web_driver, chrome.WebDriver) or
                isinstance(web_driver, firefox.WebDriver)):
            break
    if not web_driver:
        yield

    scr_name = node.nodeid.split("::")[-1]
    if SAVE_ERROR_SCREENSHOTS:
        scr_path = "./error_screenshots"
        Path(scr_path).mkdir(parents=True, exist_ok=True)
        web_driver.save_screenshot(f"{scr_path}/{scr_name}.png")

    allure.attach(
        name=scr_name,
        body=web_driver.get_screenshot_as_png(),
        attachment_type=allure.attachment_type.PNG)
    yield

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
