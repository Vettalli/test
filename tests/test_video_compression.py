from config import config
from page_objects.compress_video_page import CompressVideoPage
from config.config import BASE_URL
from page_objects.home_page import HomePage
from utils.file_utils import get_file_size, get_latest_file


def test_video_compression(driver):
    home_page = HomePage(driver)
    compress_video_page = CompressVideoPage(driver)

    home_page.open(BASE_URL)
    home_page.go_to_compress_videos()

    compress_video_page.upload_video(config.ORIGINAL_VIDEO_FILE_DIR)

    compress_video_page.wait_for_compression_finish()
    compress_video_page.click_download()
    compress_video_page.wait_for_download(config.DOWNLOAD_DIR)

    original = get_file_size(config.ORIGINAL_VIDEO_FILE_DIR)
    downloaded = get_file_size(get_latest_file(config.DOWNLOAD_DIR))

    assert downloaded < original, \
    f"Compressed file is not smaller! downloaded={downloaded}, original={original}"

