import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = 1310
    browser.config.window_height = 1410
    browser.config.driver_name = 'chrome'

    yield

    browser.quit()
