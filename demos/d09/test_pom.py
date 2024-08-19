import pytest
from playwright.sync_api import Page

from pom_model import App2Page


@pytest.fixture(scope="function", autouse=True)
def the_page(page: Page):
    app2_page_fixture = App2Page(page)
    app2_page_fixture.navigate()
    return app2_page_fixture


def test_correct_error_is_displayed_when_both_fields_are_empty(the_page):
    the_page.validate()
    the_page.should_show_both_errors()
    the_page.should_hide_first_name_error()
    the_page.should_hide_last_name_error()


def test_correct_error_is_displayed_when_only_first_name_is_empty(the_page):
    the_page.type_anything_in_last_name()
    the_page.validate()
    the_page.should_show_first_name_error()
    the_page.should_hide_last_name_error()
    the_page.should_hide_both_errors()


def test_correct_error_is_displayed_when_only_last_name_is_empty(the_page):
    the_page.type_anything_in_first_name()
    the_page.validate()
    the_page.should_hide_first_name_error()
    the_page.should_show_last_name_error()
    the_page.should_hide_both_errors()


def test_no_error_is_shown_if_both_fields_are_filled(the_page):
    the_page.type_anything_in_first_name()
    the_page.type_anything_in_last_name()
    the_page.validate()
    the_page.should_hide_first_name_error()
    the_page.should_hide_last_name_error()
    the_page.should_hide_both_errors()


def test_typing_anything_clears_both_empty_error(the_page):
    the_page.validate()
    the_page.type_anything_in_first_name()
    the_page.should_hide_both_errors()


def test_typing_anything_clears_first_empty_error(the_page):
    the_page.type_anything_in_last_name()
    the_page.validate()
    the_page.type_anything_in_first_name()
    the_page.should_hide_last_name_error()


def test_typing_anything_clears_last_empty_error(the_page):
    the_page.type_anything_in_first_name()
    the_page.validate()
    the_page.type_anything_in_last_name()
    the_page.should_hide_first_name_error()


def test_typing_anything_on_non_empty_field_clears_empty_error(the_page):
    the_page.type_anything_in_first_name()
    the_page.validate()
    the_page.type_anything_in_first_name()
    the_page.should_hide_first_name_error()

    the_page.clear_both()

    the_page.type_anything_in_last_name()
    the_page.validate()
    the_page.type_anything_in_last_name()
    the_page.should_hide_last_name_error()
