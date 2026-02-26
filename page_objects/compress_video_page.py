from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
from selenium.webdriver.common.by import By
from page_objects.base.base_page import BasePage


class CompressVideoPage(BasePage):

    DROP_ZONE = (By.XPATH, "//input[@type='file']")
    UPLOADER_PROGRESSBAR = (By.XPATH, "//*[@class = 'uploader-progressbar']")
    CIRCLE_LOADING = (By.XPATH, "//*[contains(@style, 'infinite normal')]")
    DOWNLOAD_BUTTON = (By.XPATH, "//*[@class = 'optimizer-download-btn']")
    RESTART_SESSION_BUTTON = (By.XPATH, "//*[@class = 'restart-btn']")
    ACCEPT = (By.XPATH, "//button[@data-tid='banner-accept']")

    def upload_video(self, file_path):

        self.wait_clickable(self.ACCEPT).click()
        file_input = self.wait.until(
            EC.presence_of_element_located(self.DROP_ZONE)
        )
        abs_path = os.path.abspath(file_path)
        file_input.send_keys(abs_path)

    def wait_for_compression_finish(self, timeout=60):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(self.UPLOADER_PROGRESSBAR))
        wait.until(EC.visibility_of_element_located(self.CIRCLE_LOADING))
        wait.until(EC.invisibility_of_element_located(self.CIRCLE_LOADING))
        wait.until(EC.visibility_of_element_located(self.DOWNLOAD_BUTTON))

    def click_download(self):
        self.click(self.DOWNLOAD_BUTTON)

    def wait_for_download(self, download_folder, timeout=60):
        seconds = 0
        while seconds < timeout:
            files = os.listdir(download_folder)
            if any(file.endswith(".mp4") for file in files):
                return
            time.sleep(1)
            seconds += 1
        raise TimeoutError("Download did not complete")