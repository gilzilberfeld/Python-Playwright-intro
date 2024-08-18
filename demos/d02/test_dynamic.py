from playwright.sync_api import Page, expect


def test_error_is_displayed_and_hidden(page: Page):
    page.goto('/a02')

    page.get_by_role("button", name= 'CHECK').click()
    error_text = page.get_by_text("Both values are missing")

    expect(error_text).to_be_visible()

    page.get_by_role("textbox", name= 'First name').fill('a')

    expect(error_text).to_be_hidden()
    # OR
    expect(error_text).not_to_be_visible()
