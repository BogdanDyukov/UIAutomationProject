import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from tests.test_data.login_data import ValidLogin, InvalidLogin


@pytest.fixture(autouse=True)
def initialize_pages(request, driver_function_scope):
    request.cls.login_page = LoginPage(driver_function_scope)
    request.cls.dashboard_page = DashboardPage(driver_function_scope)


@pytest.fixture(autouse=True)
def screenshot_after_test(request, driver_function_scope):
    yield
    allure.attach(
        body=driver_function_scope.get_screenshot_as_png(),
        name=request.node.name,
        attachment_type=allure.attachment_type.PNG
    )


@allure.feature("Авторизация")
class TestLogin:

    login_page: LoginPage
    dashboard_page: DashboardPage

    @allure.story("Авторизация с корректными учетными данными")
    @allure.title("Авторизация с валидными данными с проверкой")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self):
        with allure.step("Открываем страницу входа и логинимся с валидными данными"):
            self.login_page.login_with(*ValidLogin.LOGIN)

        with allure.step("Вход выполнен успешно! Открыта страница Dashboard"):
            self.dashboard_page.is_page_opened()
            self.dashboard_page.expect_dashboard_header()

    @allure.story("Авторизация с некорректными учетными данными")
    @allure.title("Попытка авторизации с пустыми полями ({case_name})")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username, password, case_name", [
        (InvalidLogin.EMPTY_FIELD, ValidLogin.PASSWORD, "пустой юзернейм"),
        (ValidLogin.USERNAME, InvalidLogin.EMPTY_FIELD, "пустой пароль"),
        (InvalidLogin.EMPTY_FIELD, InvalidLogin.EMPTY_FIELD, "оба поля пусты")
    ], ids=["empty_username", "empty_password", "empty_both"])
    def test_empty_credentials(self, username, password, case_name):
        with allure.step("Открываем страницу входа и логинимся с некорректными данными"):
            self.login_page.login_with(username, password)

        if not username and not password:
            with allure.step("Вход не выполнен. Под каждым пустым полем появляется текст 'Required'"):
                self.login_page.is_both_required_displayed()
        else:
            with allure.step("Вход не выполнен. Под пустым полем появляется текст 'Required'"):
                self.login_page.is_only_required_displayed()

    @allure.story("Авторизация с некорректными учетными данными")
    @allure.title("Попытка авторизации с инвалидными данными ({case_name})")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username, password, case_name", [
        (InvalidLogin.INVALID_USERNAME, ValidLogin.PASSWORD, "некорректный юзернейм"),
        (ValidLogin.USERNAME, InvalidLogin.INVALID_PASSWORD, "некорректный пароль"),
        (InvalidLogin.INVALID_USERNAME, InvalidLogin.INVALID_PASSWORD, "оба поля некорректны")
    ], ids=["invalid_username", "invalid_password", "invalid_both"])
    def test_invalid_credentials(self, username, password, case_name):
        with allure.step("Открываем страницу входа и логинимся с некорректными данными"):
            self.login_page.login_with(username, password)

        with allure.step("Вход не выполнен. Получено 'Invalid credentials'"):
            self.login_page.is_invalid_credentials_displayed()
