import os
from pathlib import Path

#browser setup
BROWSER = "chrome"
HEADLESS = False
TIMEOUT = 5

#directories
BASE_DIR = Path(__file__).resolve().parents[1]
DOWNLOAD_DIR = os.path.join(BASE_DIR, "download")
ORIGINAL_VIDEO_FILE_DIR = os.path.join(BASE_DIR, "data", "test.mp4")

#urls
BASE_URL = "https://jpegmini.com/"

