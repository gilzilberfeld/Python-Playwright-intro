from playwright.sync_api import BrowserContext, Browser

import common

app_url = "%sa01" % common.BASE_URL


def test_opening_same_page_in_same_browser_window(context: BrowserContext):
    first_page = context.new_page()
    first_page.goto(app_url)

    second_page = context.new_page()
    second_page.goto(app_url)


def test_opening_same_page_in_different_browser_windows(browser: Browser):
    first_page = browser.new_page()
    first_page.goto(app_url)

    second_page = browser.new_page()
    second_page.goto(app_url)
