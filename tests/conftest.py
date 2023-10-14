import pytest

from selenium import webdriver
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.base_url = 'https://github.com/'
    options.window_width = 1310
    options.window_height = 1410
    options.driver_name = 'chrome'
    options.browser_version = '2.37'

    yield

    browser.quit()
