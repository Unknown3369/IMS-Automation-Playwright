import pytest
import pytest_html
from datetime import datetime
import os
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://automationqa.variantqa.himshang.com.np/",
        help="IMS application URL"
    )

    parser.addoption(
        "--username",
        action="store",
        default="AutomationUser",
        help="IMS username"
    )

    parser.addoption(
        "--password",
        action="store",
        default="Test@1234",
        help="IMS password"
    )


@pytest.fixture
def config_data(request):
    return {
        "url": request.config.getoption("--url"),
        "username": request.config.getoption("--username"),
        "password": request.config.getoption("--password"),
    }


# Browser is now created and closed for EVERY TEST
@pytest.fixture
def browser():
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            args=[
                "--kiosk-printing",
                "--disable-print-preview",
            ]
        )

        yield browser

        # Close browser after test
        browser.close()
        print("\nBrowser closed after test.")


@pytest.fixture
def page(browser, config_data):

    context = browser.new_context(
        accept_downloads=True
    )

    page = context.new_page()

    # Open URL provided from terminal
    page.goto(config_data["url"])

    yield page

    # Close context after test
    if not page.is_closed():
        page.close()

    context.close()

    print("Page and context closed after test.")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        page = item.funcargs.get("page")

        if page and not page.is_closed():

            os.makedirs("Reports/screenshots", exist_ok=True)

            screenshot_path = (
                f"Reports/screenshots/"
                f"{item.name}_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )

            try:
                page.screenshot(
                    path=screenshot_path,
                    full_page=True
                )

                print(f"Screenshot saved: {screenshot_path}")

            except Exception as e:
                print(f"Screenshot capture failed: {e}")
                return

            # Attach screenshot to pytest-html report
            extras = getattr(report, "extras", [])

            extras.append(
                pytest_html.extras.png(screenshot_path)
            )

            report.extras = extras