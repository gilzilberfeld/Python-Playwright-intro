import pytest
from playwright.sync_api import Page, expect


# for /a02
class Locators:

    def __init__(self):
        self.firstNameBox = None
        self.lastNameBox = None
        self.lastNameErrorText = None
        self.firstNameErrorText = None
        self.bothErrorText = None
        self.button = None
        self.the_button = None
        self.the_label = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a02")
    locators.button = page.get_by_role("button", name="CHECK")
    locators.bothErrorText = page.get_by_text("Both values are missing")
    locators.firstNameErrorText = page.get_by_text("First name is missing")
    locators.lastNameErrorText = page.get_by_text("Last name is missing")
    locators.firstNameBox = page.get_by_role("textbox", name="First Name")
    locators.lastNameBox = page.get_by_role("textbox", name="Last Name")

    yield


@pytest.mark.a02_displaying_errors
def test_correct_error_is_displayed_when_both_fields_are_empty(locators):
    locators.button.click()
    expect(locators.bothErrorText).to_be_visible()
    expect(locators.firstNameErrorText).to_be_hidden()
    expect(locators.lastNameErrorText).to_be_hidden()


@pytest.mark.a02_displaying_errors
def test_correct_error_is_displayed_when_only_first_name_is_empty(locators):
    locators.lastNameBox.fill("a")
    locators.button.click()
    expect(locators.firstNameErrorText).to_be_visible()
    expect(locators.bothErrorText).to_be_hidden()
    expect(locators.lastNameErrorText).to_be_hidden()


@pytest.mark.a02_displaying_errors
def test_correct_error_is_displayed_when_only_last_name_is_empty(locators):
    locators.firstNameBox.fill("a")
    locators.button.click()
    expect(locators.lastNameErrorText).to_be_visible()
    expect(locators.bothErrorText).to_be_hidden()
    expect(locators.firstNameErrorText).to_be_hidden()


@pytest.mark.a02_displaying_errors
def test_no_error_is_shown_if_both_fields_are_filled(locators):
    locators.firstNameBox.fill("a")
    locators.lastNameBox.fill("a")
    locators.button.click()
    expect(locators.lastNameErrorText).to_be_hidden()
    expect(locators.firstNameErrorText).to_be_hidden()
    expect(locators.bothErrorText).to_be_hidden()


@pytest.mark.a02_clearing_errors
def test_typing_anything_clears_both_empty_error(locators):
    locators.button.click()
    locators.firstNameBox.fill("a")
    expect(locators.bothErrorText).to_be_hidden()


@pytest.mark.a02_clearing_errors
def test_typing_anything_clears_first_empty_error(locators):
    locators.lastNameBox.fill("a")
    locators.button.click()
    locators.firstNameBox.fill("a")
    expect(locators.lastNameErrorText).to_be_hidden()


@pytest.mark.a02_clearing_errors
def test_typing_anything_clears_last_empty_error(locators):
    locators.firstNameBox.fill("a")
    locators.button.click()
    locators.lastNameBox.fill("a")
    expect(locators.firstNameErrorText).to_be_hidden()


@pytest.mark.a02_clearing_errors
def test_typing_anything_on_non_empty_field_clears_empty_error(locators):
    locators.firstNameBox.fill("a")
    locators.button.click()
    locators.firstNameBox.fill("b")
    expect(locators.firstNameErrorText).to_be_hidden()

    locators.firstNameBox.clear()
    locators.lastNameBox.clear()

    locators.lastNameBox.fill("a")
    locators.button.click()
    locators.lastNameBox.fill("b")
    expect(locators.lastNameErrorText).to_be_hidden()
