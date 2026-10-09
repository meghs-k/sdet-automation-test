
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    """Page Object for DuckDuckGo search."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get("https://duckduckgo.com/")

    def search(self, book_name):
        search_box = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        search_box.send_keys(f"{book_name}")
        search_box.submit()

    def click_images(self):
        images = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#react-duckbar a[href*='ia=images']")
            )
        )
        images.click()
