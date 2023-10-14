import pytest

from selene.support.shared import config
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    config.driver_options = options
    config.base_url = 'https://github.com/'
    config.window_width = 1310
    config.window_height = 1410
    config.timeout = 15
