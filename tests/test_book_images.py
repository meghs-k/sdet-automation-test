import re
import pytest

from pages.search_page import SearchPage
from pages.image_page import ImagesPage
from utils.image_validator import validate_image_size


# TEST DATA
@pytest.mark.parametrize(
    "book_name",
    [
        "Blindness",
        "The Miserable"
    ]
)
def test_third_image_is_public_domain_and_large(driver, book_name):
    # 1. Open DuckDuckGo
    search_page = SearchPage(driver)
    search_page.open()

    # 2. Search for the book
    search_page.search(book_name)

    # 3. Select Images
    search_page.click_images()

    # 4, 5 and 6. Apply filters
    images_page = ImagesPage(driver)
    images_page.dismiss_browser_upgrade_popup()
    images_page.apply_filters()

    # 7. Get the third result
    third_result = images_page.get_third_result()
    result_text = third_result.text

    # 8. Verify source domain
    failures = []

    source_url = images_page.get_source_url(third_result)

    if not source_url:
        failures.append("Could not find the source URL")
    elif "publicdomainpictures.net" not in source_url.lower():
        failures.append(
            f"Expected publicdomainpictures.net, but got: {source_url}"
        )

    # 9. Extract displayed dimensions
    match = re.search(
        r"(\d{3,5})\s*[×xX]\s*(\d{3,5})",
        result_text
    )

    if not match:
        failures.append(
            "Could not find image dimensions in the third result text"
        )
    else:
        width = int(match.group(1))
        height = int(match.group(2))

        print(f"Displayed dimensions: {width} x {height}")

        image_size_errors = validate_image_size(width, height)
        failures.extend(image_size_errors)

    assert not failures, "Failures:\n" + "\n".join(failures)