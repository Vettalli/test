from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import re
from selenium.webdriver.common.by import By
from page_objects.base.base_page import BasePage


class CompressVideoPage(BasePage):

    DROP_ZONE = (By.XPATH, "//input[@type='file']")
    UPLOADER_PROGRESSBAR = (By.XPATH, "//*[@class = 'uploader-progressbar']")
    CIRCLE_LOADING = (By.XPATH, "//*[contains(@style, 'infinite normal')]")
    DOWNLOAD_BUTTON = (By.XPATH, "//*[@class = 'optimizer-download-btn']")
    ACCEPT = (By.XPATH, "//button[@data-tid='banner-accept']")
    ORIGINAL_SIZE = (By.XPATH, "//div[normalize-space()='Original size']/following-sibling::div[@class='size-value']")
    OUTPUT_SIZE = (By.XPATH, "//div[normalize-space()='Output size']/following-sibling::div[@class='size-value']")
    SAVED_VALUE = (By.XPATH, "//*[@class='gauge-value']")

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

    def get_original_size(self):
        text = self.wait.until(
            EC.visibility_of_element_located(self.ORIGINAL_SIZE)
        ).text
        return self._convert_to_mb(text)

    def get_output_size(self):
        text = self.wait.until(
            EC.visibility_of_element_located(self.OUTPUT_SIZE)
        ).text
        return self._convert_to_mb(text)

    def verify_saved_value_present(self):
        self.wait.until(
            EC.visibility_of_element_located(self.SAVED_VALUE)
        )

    def assert_compression_reduced_size(self):
        original = self.get_original_size()
        output = self.get_output_size()

        assert output < original, \
            f"Compression failed: output {output} MB >= original {original} MB"

    def _convert_to_mb(self, text):
        text = text.upper()
        number = float(re.search(r"[\d.]+", text).group())

        if "KB" in text:
            return number / 1024
        elif "MB" in text:
            return number
        elif "GB" in text:
            return number * 1024
        else:
            raise ValueError(f"Unknown size unit in text: {text}")