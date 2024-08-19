import pytest
from playwright.sync_api import expect, BrowserContext

# for a08
# Open the app on two pages in a browser
# Write a test plan and implement for the chat functionality
# Use common.BASE_URL + /a08,  instead of just /a08
import common

app_url = "%sa08" % common.BASE_URL


class Locators:

    def __init__(self):
        self.input2 = None
        self.log2 = None
        self.refresh_button2 = None
        self.reset_button2 = None
        self.send_button2 = None
        self.input1 = None
        self.log1 = None
        self.refresh_button1 = None
        self.reset_button1 = None
        self.send_button1 = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(context: BrowserContext, locators):
    page1 = context.new_page()
    page2 = context.new_page()
    page1.goto(app_url)
    page2.goto(app_url)

    locators.log1 = page1.get_by_role("textbox", name="log")
    locators.input1 = page1.get_by_role("textbox", name="Input")
    locators.send_button1 = page1.get_by_role("button", name="Send")
    locators.reset_button1 = page1.get_by_role("button", name="Reset")
    locators.refresh_button1 = page1.get_by_role("button", name="Refresh")

    locators.log2 = page2.get_by_role("textbox", name="log")
    locators.input2 = page2.get_by_role("textbox", name="Input")
    locators.send_button2 = page2.get_by_role("button", name="Send")
    locators.reset_button2 = page2.get_by_role("button", name="Reset")
    locators.refresh_button2 = page2.get_by_role("button", name="Refresh")


def test_startup(locators):
    expect(locators.send_button1).to_be_enabled()
    expect(locators.reset_button1).to_be_enabled()
    expect(locators.refresh_button1).to_be_enabled()
    expect(locators.log1).to_have_value("Log")
    expect(locators.input1).to_be_empty()

    expect(locators.send_button2).to_be_enabled()
    expect(locators.reset_button2).to_be_enabled()
    expect(locators.refresh_button2).to_be_enabled()
    expect(locators.log2).to_have_value("Log")
    expect(locators.input2).to_be_empty()


@pytest.mark.skip(reason="Under construction")
def test_refreshing_shows_an_empty_log(locators):
    locators.refresh_button1.click()
    expect(locators.log1).to_contain_text("Start here->")


@pytest.mark.skip(reason="Under construction")
def test_sending_and_refreshing_on_the_same_page(locators):
    locators.input1.fill('abc')
    locators.send_button1.click()
    locators.refresh_button1.click()
    expect(locators.log1).to_contain_text("abc")


def test_sending_resetting_and_refreshing_clears_the_log_on_the_same_page(locators):
    locators.input1.fill('abc')
    locators.send_button1.click()
    locators.reset_button1.click()
    locators.refresh_button1.click()
    expect(locators.log1).not_to_contain_text("abc")


@pytest.mark.skip(reason="Under construction")
def test_sending_on_page_1_then_refreshing_on_page_2(locators):
    locators.input1.fill('abc')
    locators.send_button1.click()
    locators.refresh_button2.click()
    expect(locators.log2).to_contain_text("abc")


def test_sending_resetting_on_page_1_then_refreshing_clears_the_log_on_page_2(locators):
    locators.input1.fill('abc')
    locators.send_button1.click()
    locators.reset_button1.click()
    locators.refresh_button2.click()
    expect(locators.log2).not_to_contain_text("abc")


@pytest.mark.skip(reason="Under construction")
def test_sending_on_page_1_sending_on_page_2_then_refreshing_on_both(locators):
    locators.input1.fill('abc')
    locators.send_button1.click()

    locators.input2.fill('def')
    locators.send_button2.click()

    locators.refresh_button1.click()
    expect(locators.log1).to_contain_text("abc\ndef")

    locators.refresh_button2.click()
    expect(locators.log2).to_contain_text("abc\ndef")
