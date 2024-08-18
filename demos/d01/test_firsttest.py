from playwright.sync_api import Page, expect


def test_reversal_of_input(page: Page):
    # Navigate to relative URL (from baseurl in pytest.ini)
    page.goto("/a01")

    # Find the input
    input_box = page.get_by_role("textbox", name = "Input")

    # Fill the input
    input_box.fill("abc")

    # Click the button
    page.get_by_role("button", name="REVERSE!").click()

    # Find the result
    result_box = page.get_by_role("textbox", name="Result")

    # Check the result contains the reverse string
    expect(result_box).to_have_value("cba")
