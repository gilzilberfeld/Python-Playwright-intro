from playwright.sync_api import Page, expect

ANY_CHARACTER = 'a'


class App2Page:

    def __init__(self, page: Page):
        self.page = page
        self.button = self.page.get_by_role("button", name="CHECK")
        self.both_error_text = page.get_by_text("Both values are missing")
        self.first_name_error_text = page.get_by_text("First name is missing")
        self.last_name_error_text = page.get_by_text("Last name is missing")
        self.first_name_box = page.get_by_role("textbox", name="First name")
        self.last_name_box = page.get_by_role("textbox", name="Last name")

    def navigate(self):
        self.page.goto("/a02")

    def validate(self):
        self.button.click()

    def should_show_first_name_error(self):
        expect(self.first_name_error_text).to_be_visible()

    def should_hide_first_name_error(self):
        expect(self.first_name_error_text).to_be_hidden()

    def should_show_last_name_error(self):
        expect(self.last_name_error_text).to_be_visible()

    def should_hide_last_name_error(self):
        expect(self.last_name_error_text).to_be_hidden()

    def should_show_both_errors(self):
        expect(self.both_error_text).to_be_visible()

    def should_hide_both_errors(self):
        expect(self.both_error_text).to_be_hidden()

    def type_anything_in_last_name(self):
        self.last_name_box.fill(ANY_CHARACTER)

    def type_anything_in_first_name(self):
        self.first_name_box.fill(ANY_CHARACTER)

    def clear_both(self):
        self.first_name_box.clear()
        self.last_name_box.clear()
