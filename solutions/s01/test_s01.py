from playwright.sync_api import Page, expect
# Exercises for a01
# 1. Try with a different input
# 2. Check that button is disabled in the beginning
# 3. Check that button is enabled after filling the input
# 4. Check that after clearing the text box button is disabled


def test_another_input(page: Page):
    page.goto("/a01")
    inputBox = page.get_by_role("textbox", name= "Input")

    inputBox.fill("def")
    page.get_by_role("button", name= "REVERSE!").click()

    resultBox = page.get_by_role("textbox", name= "Result" )

    expect(resultBox).to_have_value("fed")


def test_button_is_disabled_in_the_beginning ( page : Page ):
    page.goto("/a01")
    theButton = page.get_by_role("button",  name= "REVERSE!" )

    expect(theButton).to_be_disabled()

def test_button_is_enabled_after_filling_the_input( page : Page):
    page.goto("/a01")
    theButton = page.get_by_role("button", name= "REVERSE!" )
    inputBox = page.get_by_role("textbox", name= "Input" )

    inputBox.fill("def")
    expect(theButton).to_be_enabled()

def test_button_is_disabled_after_clearing_the_input( page : Page):
    page.goto("/a01")
    theButton = page.get_by_role("button",  name= "REVERSE!" )
    inputBox = page.get_by_role("textbox",  name= "Input" )

    inputBox.fill("def")
    inputBox.clear()
    expect(theButton).to_be_disabled()
