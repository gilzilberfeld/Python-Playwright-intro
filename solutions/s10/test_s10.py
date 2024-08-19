import re

import pytest
from playwright.sync_api import Page, expect, Playwright

import common


# For      a12
# APIs :   a12/storage
# 1. Write a test that proves the operation succeeded

@pytest.mark.skip("Under construction")
def test_adding_name_works_correctly(page: Page, playwright: Playwright):
    page.goto("/a12")

    the_button = page.get_by_role("button", name="Store")
    the_name = page.get_by_role("textbox", name="Name")

    the_name.fill("abc")
    the_button.click()

    # The URL contains the name as parameter
    page.wait_for_url(re.compile('a12/thankyou'))
    assert "abc" in page.url
    # expect(page.url).to_contain_text('abc')

    # The message contains the name
    the_message = page.get_by_text("Thank you").first
    expect(the_message).to_contain_text('abc')

    # The API returned 200
    get_name_api = playwright.request.new_context().get(common.STORAGE_API)
    assert get_name_api.ok

    # The returned value is correct
    the_value = get_name_api.json()
    assert the_value["theName"] == 'abc'
