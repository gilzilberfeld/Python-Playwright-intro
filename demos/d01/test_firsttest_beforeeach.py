import pytest
from playwright.sync_api import Page, expect


class Locators:

    def __init__(self):
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

    yield


def test_reversal_of_input(page: Page,locators):
    locators.input_box.fill("abc")
    page.get_by_role("button", name="REVERSE!").click()
    expect(locators.result_box).to_have_value("cba")
