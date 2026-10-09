import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ImagesPage:
    """Page Object for DuckDuckGo image results and filters."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def _click_text(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//*[normalize-space()='{text}']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    def dismiss_browser_upgrade_popup(self):
        try:
            # Wait up to 5 seconds for the close button to be clickable
            close_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[data-testid="serp-popover-promo-close"]')
                )
            )
            close_button.click()
        except TimeoutException:
            # If the pop-up doesn't appear during the run, bypass safely
            pass

    def disable_country_filter(self):
        toggle = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,'div[data-testid="web-vertical"] input[aria-label="Filter by the selected region"]'
                )
            )
        )

        if toggle.is_selected():
            self.driver.execute_script("arguments[0].click();",toggle)

    def select_filter(self, filter_name, option):
        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//button[contains(., '{filter_name}')]"
                )
            )
        ).click()

        self._click_text(option)

    def apply_filters(self):
        self.disable_country_filter()
        self.select_filter("All sizes", "Wallpaper")
        self.select_filter("All Licenses", "Public Domain")

    def get_third_result(self):
        locator = (By.CSS_SELECTOR, "section ol li figure")
        time.sleep(5)
        self.wait.until(lambda d: len(d.find_elements(*locator)) >= 3)
        results = self.driver.find_elements(*locator)
        return results[2]

    def get_source_url(self, result):
        """Return the source URL of the image result."""
        for a in result.find_elements(By.TAG_NAME, "a"):
            href = a.get_attribute("href")
            if href:
                return href
        return None


    def get_image_url(self, result):
        image = result.find_element(By.TAG_NAME, "img")

        for attribute in ("data-original", "data-src", "src"):
            url = image.get_attribute(attribute)
            if url and url.startswith(("http://", "https://")):
                return url

        raise AssertionError("Could not find an image URL for the third result")
