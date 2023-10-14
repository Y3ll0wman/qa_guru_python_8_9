import pytest

from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = 1310
    browser.config.window_height = 1410
    browser.config.driver_name = 'chrome'

    yield

    browser.quit()
