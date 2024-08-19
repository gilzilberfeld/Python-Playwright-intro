import pytest, os, re
from playwright.sync_api import Page

GOOGLE_JPG = "Google.jpg"

TESTIN_GIL_JPG = "TestinGil.jpg"

WIKIPEDIA_JPG = "Wikipedia.jpg"


# for a10
# write three test that create a screenshot including each frame content
# clean up the files afterwards

class Locators:

  def __init__(self):
      self.wikiButton = None
      self.testingilButton = None
      self.theFrame = None
      self.googleButton = None


@pytest.fixture(scope="module")
def locators():
  return Locators()


@pytest.fixture(scope="function", autouse=True)
def before_after_each(page: Page, locators):
    page.goto("/a10")
    locators.googleButton = page.get_by_role("button", name= "Google")
    locators.testingilButton = page.get_by_role("button", name= "TestinGil")
    locators.wikiButton = page.get_by_role("button", name= "Wikipedia" )
    locators.theFrame = page.main_frame.child_frames[0]

    yield

    if os.path.exists(WIKIPEDIA_JPG):
        os.remove(WIKIPEDIA_JPG)
    if os.path.exists(TESTIN_GIL_JPG):
        os.remove(TESTIN_GIL_JPG)
    if os.path.exists(GOOGLE_JPG):
        os.remove(GOOGLE_JPG)

def test_grab_screenshots_of_Google_frame(page:Page, locators):
   locators.googleButton.click()
   locators.theFrame.wait_for_url (re.compile("google"))
   page.screenshot( path = "Google.jpg")


def test_grab_screenshots_of_TestinGil_frame(page:Page ,locators):
   locators.testingilButton.click()
   locators.theFrame.wait_for_url (re.compile("everydayunittesting"))
   page.screenshot( path= "TestinGil.jpg")


def test_grab_screenshots_of_Wikipedia_frame(page:Page, locators):
   locators.wikiButton.click()
   locators.theFrame.wait_for_url (re.compile("wikipedia"))
   page.screenshot(path="Wikipedia.jpg")


