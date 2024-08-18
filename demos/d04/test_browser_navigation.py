from playwright.sync_api import Page, expect


def test_browser_navigation(page: Page):
    page.goto('/a03')

    input_box = page.get_by_role("textbox", name="Input")
    button = page.get_by_role("button", name='Go to Reverse Page')
    message = page.get_by_text('The reverse of')

    input_box.fill('navigate')
    button.click()

    expect(page).to_have_url('a03/reverse?input=navigate')

    page.go_back()
    expect(page).to_have_url('/a03')

    expect(input_box).to_be_empty()

    page.go_forward()
    expect(message).to_contain_text('etagivan')
