# JPEGmini Selenium tests

## Requirements

- Python 3.10+ recommended
- Google Chrome installed

## Install

Create and activate a virtual environment, then install dependencies.

**Required packages** (at minimum):

```bash
pip install selenium webdriver-manager
```

Suggested (to run tests):

```bash
pip install pytest
```

## Project files you may need to configure

- `config/config.py`
  - `BASE_URL`: target site
  - `DOWNLOAD_DIR`: download folder (created automatically by `conftest.py`)
  - `ORIGINAL_VIDEO_FILE_DIR`: path to the input video (default: `data/test.mp4`)
  - `HEADLESS`: set to `True` for headless runs

## Test data

Place a test video at:

- `data/test.mp4`

## Run tests

From the project root:

```bash
pytest -q
```

## Notes

- Downloads are saved into `download/` (relative to the project root).
- `CompressVideoPage.wait_for_compression_finish()` waits for the upload/progress UI and the download button before attempting to download.

