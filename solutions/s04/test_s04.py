import pytest
from playwright.sync_api import Page, expect


# for a05
# The buttons change state when checking the checkbox
# Checkboxes affect the buttons
# 	    1. Write a test plan
#       2. Write the tests that the behavior of buttons and checkbox is as expected
class Locators:

    def __init__(self):
        self.selectBothButton = None
        self.checkbox2 = None
        self.checkbox1 = None
        self.clearBothButton = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a05")
    locators.clearBothButton = page.get_by_role("button", name="Clear both")
    locators.selectBothButton = page.get_by_role("button", name="Select both")
    locators.checkbox1 = page.get_by_role("checkbox", name="Check 1")
    locators.checkbox2 = page.get_by_role("checkbox", name="Check 2")


def test_on_startup_both_checkboxes_are_unchecked_and_clear_is_disabled(locators):
    expect(locators.checkbox1).not_to_be_checked()
    expect(locators.checkbox2).not_to_be_checked()
    expect(locators.selectBothButton).to_be_enabled()
    expect(locators.clearBothButton).to_be_disabled()


def test_selecting_both_when_both_unchecked_checks_both_and_disables_select_all_button(locators):
    locators.selectBothButton.click()

    expect(locators.checkbox1).to_be_checked()
    expect(locators.checkbox2).to_be_checked()
    expect(locators.selectBothButton).to_be_disabled()
    expect(locators.clearBothButton).to_be_enabled()


def test_selecting_both_when_one_unchecked_checks_both_and_disables_select_all_button(locators):
    locators.checkbox1.check()
    locators.selectBothButton.click()

    expect(locators.checkbox1).to_be_checked()
    expect(locators.checkbox2).to_be_checked()
    expect(locators.selectBothButton).to_be_disabled()
    expect(locators.clearBothButton).to_be_enabled()


def test_clearing_both_when_one_is_unchecked_clears_and_disables_clear(locators):
    locators.checkbox2.check()
    locators.clearBothButton.click()

    expect(locators.checkbox1).not_to_be_checked()
    expect(locators.checkbox2).not_to_be_checked()
    expect(locators.selectBothButton).to_be_enabled()
    expect(locators.clearBothButton).to_be_disabled()


def test_clearing_all_when_both_checked_clears_and_disables_clear(locators):
    locators.checkbox1.check()
    locators.checkbox2.check()
    locators.clearBothButton.click()

    expect(locators.checkbox1).not_to_be_checked()
    expect(locators.checkbox2).not_to_be_checked()
    expect(locators.selectBothButton).to_be_enabled()
    expect(locators.clearBothButton).to_be_disabled()


def test_checking_one_enables_both_buttons(locators):
    locators.checkbox1.check()

    expect(locators.selectBothButton).to_be_enabled()
    expect(locators.clearBothButton).to_be_enabled()


def test_checking_one_and_unchecking_disables_the_clear_button(locators):
    locators.checkbox1.check()
    locators.checkbox1.uncheck()

    expect(locators.selectBothButton).to_be_enabled()
    expect(locators.clearBothButton).to_be_disabled()


def test_selecting_both_and_unchecking_one_enables_both_buttons(locators):
    locators.selectBothButton.click()
    locators.checkbox2.uncheck()

    expect(locators.selectBothButton).to_be_enabled()
    expect(locators.clearBothButton).to_be_enabled()


def test_checking_both_disables_the_select_button(locators):
    locators.checkbox1.check()
    locators.checkbox2.check()

    expect(locators.selectBothButton).to_be_disabled()
    expect(locators.clearBothButton).to_be_enabled()
