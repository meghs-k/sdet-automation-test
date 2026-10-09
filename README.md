# **Project Overview**

This project automates the DuckDuckGo image search scenario using Python, Selenium, and Pytest.

The test searches for a book, applies image filters, and validates the third image result.

## **Test Scenario**

The automation performs the following steps:

1.Open DuckDuckGo.

2.Search for book {BOOK_NAME}.

3.Select the Images tab.

4.Disable the country/region filter if it is enabled.

5.Select the Wallpaper size filter.

6.Select the Public Domain license filter.

7.Verify that the third image result belongs to publicdomainpictures.net.

8.Read the image width and height displayed on the third result card and verify that both dimensions are greater than 1000 pixels.

9.Capture a screenshot if the test fails.

## Technologies Used

- Python – Programming language
- Selenium – Browser automation
- Pytest – Test execution and parametrization
- pytest-html – Generating an HTML test report

## **How the Code Works**

1. pages/search_page.py

Contains the actions required to open DuckDuckGo, search for a book, and select Images.

2. pages/image_page.py

Contains the image-page actions, including disabling the region filter, selecting Wallpaper and Public Domain, and retrieving the third image result.

3. tests/test_book_images.py

Contains the main test scenario and the assertions.

1.Open DuckDuckGo: Navigate to the DuckDuckGo website.
2.Search for a book: Search using the keyword book {BOOK_NAME}.
3.Select Images: Open the Images tab.
4.Disable country/region filter: Disable the filter if it is enabled.
5.Apply image filters: Select the Wallpaper size and Public Domain license filters.
6.Get the third result: Locate the third image result after applying the filters.
7.Validate the source: Check whether the source URL contains publicdomainpictures.net.
8.Extract image dimensions: Use a regular expression to extract the displayed width and height from the result text.
9.Validate dimensions: Call validate_image_size(width, height) to verify that both dimensions are greater than 1000 pixels.
10.Report failures: Collect validation errors and fail the test if any check fails.

**Parameterized testing**

The test runs for multiple book names, including Blindness and The Miserable, using Pytest parameterization.

4.utils/image_validator.py

The validate_image_size(width, height) function validates the image dimensions displayed on the third DuckDuckGo image result card.

- Receives the extracted image width and height as arguments.
- Checks whether the width is greater than 1000 pixels.
- Checks whether the height is greater than 1000 pixels.
- Adds an error message for each dimension that does not meet the requirement.
- Returns a list of validation errors. An empty list indicates that both dimensions passed validation

5. conftest.py

Contains the Pytest fixture and failure-screenshot handling. When a test fails during execution, a screenshot of the current browser page is saved in the screenshots/ folder.

6. pytest.ini

Contains the basic Pytest configuration.

7. requirements.txt

Lists the Python packages needed to run the project.

Run the Tests

**Execute the tests using:**

pytest

**Generate an HTML Report**

Run:

pytest --html=report.html --self-contained-html

Open report.html in a browser to view the test results.

**Failure Screenshots**

If a test fails, the screenshot is saved in the screenshots/ folder for debugging.

**Design Approach**

- This project uses the Page Object Model (POM) to separate browser interactions from test logic.
- Page classes contain page actions and locators.
- The test file describes the test scenario and assertions.
- The utility module validates image dimensions.
- Pytest fixtures manage browser setup and cleanup.
- This structure keeps the automation simple, readable, and maintainable.