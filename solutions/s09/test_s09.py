import os
import pytest
import re
from playwright.sync_api import Page

GOOGLE_JPG = "Google.jpg"

TESTINGIL_JPG = "TestinGil.jpg"

WIKIPEDIA_JPG = "Wikipedia.jpg"


# for a10
# write three test that create a screenshot including each frame content
# clean up the files afterwards

class Locators:

    def __init__(self):
        self.wiki_button = None
        self.testingil_button = None
        self.the_frame = None
        self.google_button = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_after_each(page: Page, locators):
    page.goto("/a10")
    locators.google_button = page.get_by_role("button", name="Google")
    locators.testingil_button = page.get_by_role("button", name="TestinGil")
    locators.wiki_button = page.get_by_role("button", name="Wikipedia")
    locators.the_frame = page.main_frame.child_frames[0]

    yield

    if os.path.exists(WIKIPEDIA_JPG):
        os.remove(WIKIPEDIA_JPG)
    if os.path.exists(TESTINGIL_JPG):
        os.remove(TESTINGIL_JPG)
    if os.path.exists(GOOGLE_JPG):
        os.remove(GOOGLE_JPG)


def test_grab_screenshots_of_google_frame(page: Page, locators):
    locators.google_button.click()
    locators.the_frame.wait_for_url(re.compile("google"))
    page.screenshot(path=GOOGLE_JPG)


def test_grab_screenshots_of_testingil_frame(page: Page, locators):
    locators.testingil_button.click()
    locators.the_frame.wait_for_url(re.compile("everydayunittesting"))
    page.screenshot(path=TESTINGIL_JPG)


def test_grab_screenshots_of_wikipedia_frame(page: Page, locators):
    locators.wiki_button.click()
    locators.the_frame.wait_for_url(re.compile("wikipedia"))
    page.screenshot(path=WIKIPEDIA_JPG)
