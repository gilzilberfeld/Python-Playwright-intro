import pytest
from playwright.sync_api import Page, expect


# for a06
# You can select items directly through the drop-down and through the text-box and the button
# The label shows the selected value
#  	1. Write a test plan
#   2. Write the tests that check the display based on selection

class Locators:

    def __init__(self):
        self.the_label = None
        self.the_text_box = None
        self.the_drop_down = None
        self.the_button = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a06")
    locators.the_button = page.get_by_role("button", name="Select")
    locators.the_drop_down = page.get_by_role("combobox")
    locators.the_text_box = page.get_by_role("textbox", name="Select Item")
    locators.the_label = page.get_by_text("Selected:")


def test_startup(locators):
    expect(locators.the_button).to_be_disabled()
    expect(locators.the_drop_down).to_have_text("Item 1")
    expect(locators.the_text_box).to_be_empty()
    expect(locators.the_label).to_have_text("Selected: Item 1")


def test_select_through_drop_down(page: Page, locators):
    locators.the_drop_down.click()
    page.get_by_role('option', name='Item 3').click()
    expect(locators.the_label).to_have_text("Selected: Item 3")


def test_entering_a_value_enables_the_button(locators):
    locators.the_text_box.fill('1')
    expect(locators.the_button).to_be_enabled()


def test_clearing_the_textbox_disables_the_button(locators):
    locators.the_text_box.fill('1')
    locators.the_text_box.clear()

    expect(locators.the_button).to_be_disabled()


def test_select_through_input(locators):
    locators.the_text_box.fill('3')
    locators.the_button.click()
    expect(locators.the_label).to_have_text("Selected: Item 3")


def test_no_item_found(locators):
    locators.the_text_box.fill('z')
    locators.the_button.click()
    expect(locators.the_label).to_have_text("Selected: Item Not Found")
