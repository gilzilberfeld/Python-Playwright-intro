import pytest
from playwright.sync_api import Page, expect, Playwright

API_URL = "https://playwright-intro.vercel.app/a11/counter"


class Locators:

    def __init__(self):
        self.the_button = None
        self.the_label = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    locators.the_button = page.get_by_role("button", name="Increment")
    locators.the_label = page.get_by_text("Counter: ")

    yield


@pytest.mark.skip(reason="because syncs")
def test_starting_from_scratch(page: Page, playwright: Playwright, locators):
    reset_api = playwright.request.new_context().post(API_URL, data={"newCounter": "0"})
    assert reset_api.ok
    reset_api.dispose()

    page.goto("/a11")
    expect(locators.the_label).to_contain_text("0")
    locators.the_button.click()
    expect(locators.the_label).to_contain_text("1")


@pytest.mark.skip(reason="because syncs")
def test_resetting_the_counter(page: Page, playwright: Playwright, locators):
    reset_api = playwright.request.new_context().post(API_URL, data={"newCounter": "5"})
    assert reset_api.ok
    reset_api.dispose()

    page.goto("/a11")
    expect(locators.the_label).to_contain_text("5")
    locators.the_button.click()
    expect(locators.the_label).to_contain_text("6")
