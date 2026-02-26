import pytest
import os
from utils.browser_setup import create_driver
from config.config import DOWNLOAD_DIR

@pytest.fixture(scope="function")
def driver():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    driver = create_driver()
    yield driver
    driver.quit()