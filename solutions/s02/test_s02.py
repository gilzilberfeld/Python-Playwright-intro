import pytest
from playwright.sync_api import Page, expect


# Exercises for a02
# 1. Create test plan for all cases and errors
# 2. Write clean tests

class Locators:

    def __init__(self):
        self.lastNameErrorText = None
        self.lastNameBox = None
        self.firstNameErrorText = None
        self.bothErrorText = None
        self.button = None
        self.firstNameBox = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a02")
    locators.bothErrorText = page.get_by_text("Both values are missing")
    locators.firstNameErrorText = page.get_by_text("First name is missing")
    locators.lastNameErrorText = page.get_by_text("Last name is missing")
    locators.button = page.get_by_role("button", name="CHECK")
    locators.firstNameBox = page.get_by_role("textbox", name="First name")
    locators.lastNameBox = page.get_by_role("textbox", name="Last name")

    yield


def test_correct_error_is_displayed_when_both_fields_are_empty(locators):
    locators.button.click()
    expect(locators.bothErrorText).to_be_visible()
    expect(locators.firstNameErrorText).to_be_hidden()
    expect(locators.lastNameErrorText).to_be_hidden()


def test_correct_error_is_displayed_when_only_first_name_is_empty(locators):
    locators.lastNameBox.fill('a')
    locators.button.click()
    expect(locators.firstNameErrorText).to_be_visible()
    expect(locators.bothErrorText).to_be_hidden()
    expect(locators.lastNameErrorText).to_be_hidden()


def test_correct_error_is_displayed_when_only_last_name_is_empty(locators):
    locators.firstNameBox.fill('a')
    locators.button.click()
    expect(locators.lastNameErrorText).to_be_visible()
    expect(locators.bothErrorText).to_be_hidden()
    expect(locators.firstNameErrorText).to_be_hidden()


def test_no_error_is_shown_if_both_fields_are_filled(locators):
    locators.firstNameBox.fill('a')
    locators.lastNameBox.fill('a')
    locators.button.click()
    expect(locators.lastNameErrorText).to_be_hidden()
    expect(locators.firstNameErrorText).to_be_hidden()
    expect(locators.bothErrorText).to_be_hidden()


def test_typing_anything_clears_both_empty_error(locators):
    locators.button.click()
    locators.firstNameBox.fill('a')
    expect(locators.bothErrorText).to_be_hidden()


def test_typing_anything_clears_first_empty_error(locators):
    locators.lastNameBox.fill('a')
    locators.button.click()
    locators.firstNameBox.fill('a')
    expect(locators.lastNameErrorText).to_be_hidden()


def test_typing_anything_clears_last_empty_error(locators):
    locators.firstNameBox.fill('a')
    locators.button.click()
    locators.lastNameBox.fill('a')
    expect(locators.firstNameErrorText).to_be_hidden()


def test_typing_anything_on_non_empty_field_clears_empty_error(locators):
    locators.firstNameBox.fill('a')
    locators.button.click()
    locators.firstNameBox.fill('b')
    expect(locators.firstNameErrorText).to_be_hidden()

    locators.firstNameBox.clear()
    locators.lastNameBox.clear()

    locators.lastNameBox.fill('a')
    locators.button.click()
    locators.lastNameBox.fill('b')
    expect(locators.lastNameErrorText).to_be_hidden()
