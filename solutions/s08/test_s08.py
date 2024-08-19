import pytest
from playwright.sync_api import expect, BrowserContext, Page


# for a10
# Make sure that in the frame appears the right image and not the other images
class Locators:

    def __init__(self):
        self.googleButton = None
        self.wikiButton = None
        self.testingilButton = None
        self.googleImage = None
        self.wikiImage = None
        self.testingilImage = None


@pytest.fixture(scope="module")
def locators():
    return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page, locators):
    page.goto("/a10")
    locators.googleButton = page.get_by_role("button", name= "Google" )
    locators.testingilButton = page.get_by_role("button", name= "TestinGil" )
    locators.wikiButton = page.get_by_role("button", name= "Wikipedia" )
    the_frame = page.main_frame.child_frames[0]
    locators.googleImage = the_frame.get_by_role('img', name = 'google')
    locators.testingilImage = the_frame.get_by_alt_text("TestinGil")
    locators.wikiImage = the_frame.locator('.central-featured-logo')

def test_google_has_google_image_and_no_testinGil_or_Wiki_image(locators):
   locators.googleButton.click()
   expect(locators.googleImage).to_be_visible()
   expect(locators.testingilImage).to_be_hidden()
   expect(locators.wikiImage).to_be_hidden()

def test_testinGil_has_testingil_image_and_no_google_or_wiki_image(locators):
   locators.testingilButton.click()
   expect(locators.testingilImage).to_be_visible()
   expect(locators.googleImage).to_be_hidden()
   expect(locators.wikiImage).to_be_hidden()


def test_Wiki_has_Wiki_image_and_no_TestinGil_Google_image(locators):
   locators.wikiButton.click()
   expect(locators.wikiImage).to_be_visible()
   expect(locators.googleImage).to_be_hidden()
   expect(locators.testingilImage).to_be_hidden()
