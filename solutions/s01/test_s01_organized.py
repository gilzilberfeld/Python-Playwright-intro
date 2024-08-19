import pytest
from playwright.sync_api import Page, expect


class Locators:

    def __init__(self):
        self.button = None
        self.result_box = None
        self.input_box = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a01")
    locators.input_box = page.get_by_role("textbox", name="Input")
    locators.result_box = page.get_by_role("textbox", name="Result")
    locators.button = page.get_by_role("button", name="REVERSE!")

    yield


def test_another_input(locators):
    locators.input_box.fill("def")
    locators.button.click()
    expect(locators.result_box).to_have_value("fed")


def test_button_is_disabled_in_the_beginning(locators):
    expect(locators.button).to_be_disabled()


def test_button_is_enabled_after_filling_the_input(locators):
    locators.input_box.fill("def")
    expect(locators.button).to_be_enabled()


def test_button_is_disabled_after_clearing_the_input(locators):
    locators.input_box.fill("def")
    locators.input_box.clear()
    expect(locators.button).to_be_disabled()
