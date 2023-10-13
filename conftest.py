import pytest
from selene.support.shared import config


@pytest.fixture(scope='function', autouse=True)
def browser_chrome():
    config.window_width = 1310
    config.window_height = 1410
