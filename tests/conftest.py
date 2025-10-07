import pytest
import sys
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import attach

def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Браузер, в котором будут запущены тесты',
        choices=['firefox', 'chrome'],
        default='chrome'
    )

@pytest.fixture(scope='function')
def setup_browser(request):
    browser_name = request.config.getoption('--browser')
    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
