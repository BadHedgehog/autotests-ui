import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, \
    Page, Playwright  # Имопртируем класс страницы, будем использовать его для аннотации типов


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page() -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Ниже идет инициализация и открытие новой страницы
    with sync_playwright() as playwright:
        # Запускаем браузер
        browser = playwright.chromium.launch(headless=False)

        # Передаем страницу для использования в тесте
        yield browser.new_page()

        # Закрываем браузер после выполнения тестов
        browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state():
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


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    yield page
