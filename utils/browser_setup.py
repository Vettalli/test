from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from config.config import DOWNLOAD_DIR, HEADLESS


def create_driver():
    chrome_options = Options()

    if HEADLESS:
        chrome_options.add_argument("--headless=new")
    else:
        chrome_options.add_argument("--start-maximized")

    chrome_options.add_argument("--ignore-certificate-errors")

    prefs = {
        "download.default_directory": os.path.abspath(DOWNLOAD_DIR),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }

    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver