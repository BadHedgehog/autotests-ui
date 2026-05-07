import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    heading = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(heading).to_have_text("Courses")

    block_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_text).to_have_text("There is no results")

    block_text_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_text_description).to_have_text("Results from the load test pipeline will be displayed here")

    block_text_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(block_text_icon).to_be_visible()
