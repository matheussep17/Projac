import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright

from config.settings import settings


@pytest.fixture(scope="session")
def browser(playwright: Playwright, pytestconfig: pytest.Config) -> Browser:
    headed = pytestconfig.getoption("headed", default=False)
    return playwright.chromium.launch(headless=False if headed else settings.headless)


@pytest.fixture()
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()
