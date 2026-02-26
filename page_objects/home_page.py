from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base.base_page import BasePage
from page_objects.compress_video_page import CompressVideoPage

class HomePage(BasePage):

    COMPRESS_VIDEOS_BUTTON = (
        By.XPATH,
        "(//a[contains(@href,'compress-videos')])[1]"
    )

    def open(self, base_url):
        self.driver.get(base_url)
        return self

    def go_to_compress_videos(self):
        original_window = self.driver.current_window_handle

        self.wait_visible(self.COMPRESS_VIDEOS_BUTTON).click()

        self.wait.until(EC.number_of_windows_to_be(2))

        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

        self.wait.until(EC.url_contains("compress-videos"))

        return CompressVideoPage(self.driver)