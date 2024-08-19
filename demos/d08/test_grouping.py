import pytest
from playwright.sync_api import Page, expect


# for /a02
class Locators:

    def __init__(self):
        self.first_name_box = None
        self.last_name_box = None
        self.last_name_error_text = None
        self.first_name_error_text = None
        self.both_error_text = None
        self.button = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a02")
    locators.button = page.get_by_role("button", name="CHECK")
    locators.both_error_text = page.get_by_text("Both values are missing")
    locators.first_name_error_text = page.get_by_text("First name is missing")
    locators.last_name_error_text = page.get_by_text("Last name is missing")
    locators.first_name_box = page.get_by_role("textbox", name="First Name")
    locators.last_name_box = page.get_by_role("textbox", name="Last Name")

    yield


@pytest.mark.a02_displaying_errors
def test_correct_error_is_displayed_when_both_fields_are_empty(locators):
    locators.button.click()
    expect(locators.both_error_text).to_be_visible()
    expect(locators.first_name_error_text).to_be_hidden()
    expect(locators.last_name_error_text).to_be_hidden()


@pytest.mark.a02_displaying_errors
def test_correct_error_is_displayed_when_only_first_name_is_empty(locators):
    locators.last_name_box.fill("a")
    locators.button.click()
    expect(locators.first_name_error_text).to_be_visible()
    expect(locators.both_error_text).to_be_hidden()
    expect(locators.last_name_error_text).to_be_hidden()


@pytest.mark.a02_displaying_errors
def test_correct_error_is_displayed_when_only_last_name_is_empty(locators):
    locators.first_name_box.fill("a")
    locators.button.click()
    expect(locators.last_name_error_text).to_be_visible()
    expect(locators.both_error_text).to_be_hidden()
    expect(locators.first_name_error_text).to_be_hidden()


@pytest.mark.a02_displaying_errors
def test_no_error_is_shown_if_both_fields_are_filled(locators):
    locators.first_name_box.fill("a")
    locators.last_name_box.fill("a")
    locators.button.click()
    expect(locators.last_name_error_text).to_be_hidden()
    expect(locators.first_name_error_text).to_be_hidden()
    expect(locators.both_error_text).to_be_hidden()


@pytest.mark.a02_clearing_errors
def test_typing_anything_clears_both_empty_error(locators):
    locators.button.click()
    locators.first_name_box.fill("a")
    expect(locators.both_error_text).to_be_hidden()


@pytest.mark.a02_clearing_errors
def test_typing_anything_clears_first_empty_error(locators):
    locators.last_name_box.fill("a")
    locators.button.click()
    locators.first_name_box.fill("a")
    expect(locators.last_name_error_text).to_be_hidden()


@pytest.mark.a02_clearing_errors
def test_typing_anything_clears_last_empty_error(locators):
    locators.first_name_box.fill("a")
    locators.button.click()
    locators.last_name_box.fill("a")
    expect(locators.first_name_error_text).to_be_hidden()


@pytest.mark.a02_clearing_errors
def test_typing_anything_on_non_empty_field_clears_empty_error(locators):
    locators.first_name_box.fill("a")
    locators.button.click()
    locators.first_name_box.fill("b")
    expect(locators.first_name_error_text).to_be_hidden()

    locators.first_name_box.clear()
    locators.last_name_box.clear()

    locators.last_name_box.fill("a")
    locators.button.click()
    locators.last_name_box.fill("b")
    expect(locators.last_name_error_text).to_be_hidden()
