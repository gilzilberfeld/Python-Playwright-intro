from playwright.sync_api import Page, expect


def test_finding_the_frame(page: Page):
    page.goto("/a09")

    number_of_frames = len(page.main_frame.child_frames)
    assert number_of_frames == 1

    the_frame = page.main_frame.child_frames[0]

    the_result_box = the_frame.get_by_role("textbox", name="Result")
    expect(the_result_box).to_have_value('Waiting...')
