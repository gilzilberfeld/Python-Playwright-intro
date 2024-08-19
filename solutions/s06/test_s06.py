from playwright.sync_api import Page, expect


# For a07
# 	1. Write a test that checks that the URLs contain the right information
#   2. Write a test that goes to page 3, then goes back twice.
#      Check that the URL and texts are displayed correctly and the input boxes are empty.


def test_navigation_through_input_is_correct(page:Page):
    page.goto("/a07")
    firstPageButton = page.get_by_role("button", name= "Go To")
    firstPageInput = page.get_by_role("textbox", name= "Input" )

    firstPageInput.fill("abc")
    firstPageButton.click()
    expect(page).to_have_url("a07/page2?input=abc")

    secondPageButton = page.get_by_role("button", name= "Go To" )
    secondPageInput = page.get_by_role("textbox", name= "Input" )

    secondPageInput.fill("def")
    secondPageButton.click()
    expect(page).to_have_url("a07/page3?input=abcdef")

def test_navigation_back_from_3rd_page_label_is_correct (page: Page):
    page.goto("/a07")

    firstPageButton = page.get_by_role("button",  name= "Go To" )
    firstPageInput = page.get_by_role("textbox", name= "Input" )

    firstPageInput.fill("abc")
    firstPageButton.click()

    page.wait_for_url("a07/page2?input=abc")

    secondPageButton = page.get_by_role("button",  name= "Go To" )
    secondPageInput = page.get_by_role("textbox",  name= "Input" )

    secondPageInput.fill("def")
    secondPageButton.click()

    page.wait_for_url("a07/page3?input=abcdef")

    page.go_back()
    expect(page).to_have_url("a07/page2?input=abc")

    secondPageText = page.get_by_text("From Page 1")
    expect(secondPageText).to_contain_text("abc")
    expect(secondPageInput).to_be_empty()

    page.go_back()
    expect(page).to_have_url("a07")

    expect(firstPageInput).to_be_empty()
