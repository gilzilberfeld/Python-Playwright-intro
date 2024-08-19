# For guru99 demo: https://demo.guru99.com/test/newtours/index.php
# 1. With CodeGen create test that checks that the descriptions of the flights are visible
#       and contain the right values.
# 2. Write a test that calculates the total the $ sums and makes sure it's 1490
#      hint: use the RegEx /^\$\d+/
import re

import pytest
from playwright.sync_api import Page, expect

import common

DOLLAR_PRICE_PATTERN = r"^\$\d+"


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    page.goto('%s' % common.GURU99_URL)


def test_tours_page_has_the_right_text(page: Page):
    expect(page.get_by_text('Atlanta to Las Vegas')).to_be_visible()
    expect(page.get_by_text('Boston to San Francisco')).to_be_visible()

    expect(page.locator('body')).to_contain_text('New York to Chicago')
    expect(page.locator('body')).to_contain_text('Phoenix to San Francisco')


def test_cells_contains_exact_total(page: Page):
    cells = page.get_by_role('cell', name=re.compile(DOLLAR_PRICE_PATTERN))
    allCells = cells.all()
    total = 0

    for cell in allCells:
        content = cell.inner_text()
        total += int(content[1:])

    assert total == 1490
