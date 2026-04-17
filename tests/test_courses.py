import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path="browser-state.json")

        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        heading = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(heading).to_have_text("Courses")

        block_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(block_text).to_have_text("There is no results")

        block_text_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(block_text_description).to_have_text("Results from the load test pipeline will be displayed here")

        block_text_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(block_text_icon).to_be_visible()
