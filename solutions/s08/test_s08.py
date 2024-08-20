import pytest
from playwright.sync_api import expect, Page


# for a10
# Make sure that in the frame appears the right image and not the other images
class Locators:

    def __init__(self):
        self.google_button = None
        self.wiki_button = None
        self.testingil_button = None
        self.google_image = None
        self.wiki_image = None
        self.testingil_image = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a10")
    locators.google_button = page.get_by_role("button", name="Google")
    locators.testingil_button = page.get_by_role("button", name="TestinGil")
    locators.wiki_button = page.get_by_role("button", name="Wikipedia")
    the_frame = page.main_frame.child_frames[0]
    locators.google_image = the_frame.get_by_role('img', name='google')
    locators.testingil_image = the_frame.get_by_alt_text("TestinGil")
    locators.wiki_image = the_frame.locator('.central-featured-logo')


def test_google_has_google_image_and_no_testingil_or_wiki_image(locators):
    locators.google_button.click()
    expect(locators.google_image).to_be_visible()
    expect(locators.testingil_image).to_be_hidden()
    expect(locators.wiki_image).to_be_hidden()


def test_testingil_has_testingil_image_and_no_google_or_wiki_image(locators):
    locators.testingil_button.click()
    expect(locators.testingil_image).to_be_visible()
    expect(locators.google_image).to_be_hidden()
    expect(locators.wiki_image).to_be_hidden()


def test_Wiki_has_wiki_image_and_no_testingil_Google_image(locators):
    locators.wiki_button.click()
    expect(locators.wiki_image).to_be_visible()
    expect(locators.google_image).to_be_hidden()
    expect(locators.testingil_image).to_be_hidden()
