import pytest
from playwright.sync_api import Page, expect


# For a04
# Write the following test cases in 3 ways of finding the boxes
# 1. On startup all boxes are empty (using getByRoll().all())
# 2. When typing in the second box, the value appears in the other two (using getByPlaceHolder)
# 3. After clearing the boxes are empty (using XPath)

class Locators:

    def __init__(self):
        self.button = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a04")
    locators.button = page.get_by_role("button", name="Clear")


def test_on_startup_all_boxes_are_empty(page: Page):
    boxes = page.get_by_role("textbox", name='Clone Box').all()
    for box in boxes:
        expect(box).to_be_empty()


def test_when_typing_in_the_second_box_the_value_appears_in_the_other_two(page: Page):
    box1 = page.get_by_placeholder("box1")
    box2 = page.get_by_placeholder("box2")
    box3 = page.get_by_placeholder("box3")

    box2.fill('100a')
    expect(box1).to_have_value('100a')
    expect(box3).to_have_value('100a')


def test_after_clearing_the_boxes_are_empty(page: Page, locators):
    box1 = page.locator('xpath=/html/body/main/section/div/div[1]/div[1]/div/input')
    box2 = page.locator('xpath=/html/body/main/section/div/div[1]/div[2]/div/input')
    box3 = page.locator('xpath=/html/body/main/section/div/div[1]/div[3]/div/input')

    box2.fill('100a')
    locators.button.click()

    expect(box1).to_be_empty()
    expect(box2).to_be_empty()
    expect(box3).to_be_empty()
