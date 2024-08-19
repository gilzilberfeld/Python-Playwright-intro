import pytest
from playwright.sync_api import Page, expect


# Exercises for a02
# 1. Create test plan for all cases and errors
# 2. Write clean tests

class Locators:

    def __init__(self):
        self.last_name_error_text = None
        self.last_name_box = None
        self.first_name_error_text = None
        self.both_error_text = None
        self.button = None
        self.first_name_box = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a02")
    locators.both_error_text = page.get_by_text("Both values are missing")
    locators.first_name_error_text = page.get_by_text("First name is missing")
    locators.last_name_error_text = page.get_by_text("Last name is missing")
    locators.button = page.get_by_role("button", name="CHECK")
    locators.first_name_box = page.get_by_role("textbox", name="First name")
    locators.last_name_box = page.get_by_role("textbox", name="Last name")

    yield


def test_correct_error_is_displayed_when_both_fields_are_empty(locators):
    locators.button.click()
    expect(locators.both_error_text).to_be_visible()
    expect(locators.first_name_error_text).to_be_hidden()
    expect(locators.last_name_error_text).to_be_hidden()


def test_correct_error_is_displayed_when_only_first_name_is_empty(locators):
    locators.last_name_box.fill('a')
    locators.button.click()
    expect(locators.first_name_error_text).to_be_visible()
    expect(locators.both_error_text).to_be_hidden()
    expect(locators.last_name_error_text).to_be_hidden()


def test_correct_error_is_displayed_when_only_last_name_is_empty(locators):
    locators.first_name_box.fill('a')
    locators.button.click()
    expect(locators.last_name_error_text).to_be_visible()
    expect(locators.both_error_text).to_be_hidden()
    expect(locators.first_name_error_text).to_be_hidden()


def test_no_error_is_shown_if_both_fields_are_filled(locators):
    locators.first_name_box.fill('a')
    locators.last_name_box.fill('a')
    locators.button.click()
    expect(locators.last_name_error_text).to_be_hidden()
    expect(locators.first_name_error_text).to_be_hidden()
    expect(locators.both_error_text).to_be_hidden()


def test_typing_anything_clears_both_empty_error(locators):
    locators.button.click()
    locators.first_name_box.fill('a')
    expect(locators.both_error_text).to_be_hidden()


def test_typing_anything_clears_first_empty_error(locators):
    locators.last_name_box.fill('a')
    locators.button.click()
    locators.first_name_box.fill('a')
    expect(locators.last_name_error_text).to_be_hidden()


def test_typing_anything_clears_last_empty_error(locators):
    locators.first_name_box.fill('a')
    locators.button.click()
    locators.last_name_box.fill('a')
    expect(locators.first_name_error_text).to_be_hidden()


def test_typing_anything_on_non_empty_field_clears_empty_error(locators):
    locators.first_name_box.fill('a')
    locators.button.click()
    locators.first_name_box.fill('b')
    expect(locators.first_name_error_text).to_be_hidden()

    locators.first_name_box.clear()
    locators.last_name_box.clear()

    locators.last_name_box.fill('a')
    locators.button.click()
    locators.last_name_box.fill('b')
    expect(locators.last_name_error_text).to_be_hidden()
