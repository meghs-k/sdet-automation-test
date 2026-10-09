import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1400,1000")
    #options.add_argument("--no-sandbox")
    #options.add_argument("--disable-dev-shm-usage")

    if os.getenv("CI"):
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    yield driver

    # Close browser after test
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Take screenshot when test fails
    outcome = yield
    report = outcome.get_result()

    # Only capture screenshots for failures during the actual test
    if report.when != "call":
        return
    if not report.failed:
        return

    # Get Selenium driver from fixture
    driver = item.funcargs.get("driver")
    if driver is None:
        return

    # Create screenshots folder
    screenshot_folder = Path("screenshots")
    screenshot_folder.mkdir(exist_ok=True)

    # Create safe file name
    file_name = (
        item.nodeid
        .replace("::", "_")
        .replace(":", "_")
        .replace("/", "_")
        .replace("\\", "_")
    )
    screenshot_path = screenshot_folder / f"{file_name}.png"

    # Take screenshot
    try:
        driver.save_screenshot(str(screenshot_path))
    except Exception:
        pass  # Browser already crashed — skip screenshot silently
