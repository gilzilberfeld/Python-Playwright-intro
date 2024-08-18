import re
from playwright.sync_api import Page, expect
def test_application_navigation(page:Page):
    page.goto('/a03')

    inputBox = page.get_by_role("textbox", name= "Input")
    button = page.get_by_role("button", name= 'Go to Reverse Page')

    inputBox.fill('navigate')
    button.click()

    # after navigation
    expect(page).to_have_url(re.compile('/.*a03/reverse'))
    # OR
    expect(page).to_have_url('a03/reverse?input=navigate')

    main_header = page.get_by_text('Welcome to the Reverse page!', exact=True)
    expect(main_header).to_be_visible()

    message = page.get_by_text('The reverse of')
    expect(message).to_contain_text('etagivan')
