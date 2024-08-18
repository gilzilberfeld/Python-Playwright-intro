from playwright.sync_api import BrowserContext, Browser

url = "https://playwright-intro.vercel.app/a01"


def test_opening_same_page_in_same_browser_window(context: BrowserContext):
    first_page = context.new_page()
    first_page.goto(url)

    second_page = context.new_page()
    second_page.goto(url)


def test_opening_same_page_in_different_browser_windows(browser: Browser):
    first_page = browser.new_page()
    first_page.goto(url)

    second_page = browser.new_page()
    second_page.goto(url)
