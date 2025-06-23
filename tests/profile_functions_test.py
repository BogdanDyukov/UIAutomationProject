import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage
from tests.test_data.profile_data import ProfileData
from tests.test_data.login_data import ValidLogin


@pytest.fixture(scope="class")
def initialize_my_info_page(request, driver_class_scope):
    request.cls.my_info_page = MyInfoPage(driver_class_scope)


@pytest.fixture(scope="class", autouse=True)
def setup_state(request, initialize_my_info_page, driver_class_scope):
    login_page = LoginPage(driver_class_scope)
    dashboard_page = DashboardPage(driver_class_scope)
    my_info_page = request.cls.my_info_page

    with allure.step("Логинимся в системе"):
        login_page.login_with(*ValidLogin.LOGIN)
        dashboard_page.is_page_opened()

    with allure.step("Переходим на страницу профиля"):
        dashboard_page.click_my_info_ref()
        my_info_page.is_page_opened()


class TestProfileFunctions:

    my_info_page: MyInfoPage

    @allure.feature("Редактирование профиля")
    @allure.story("Изменение ФИО пользователя")
    @allure.title("Смена first name на {new_first_name}")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("new_first_name", [ProfileData.FIRST_NAME])
    def test_change_profile_first_name(self, new_first_name):
        with allure.step(f"Помещаем в текстовое поле значение {new_first_name}"):
            self.my_info_page.update_first_name_field(new_first_name)

        with allure.step("Сохраняем изменения"):
            self.my_info_page.click_save_button()
            self.my_info_page.wait_for_spinner_to_disappear()

        with allure.step("Убеждаемся в том, что изменения применились"):
            self.my_info_page.is_first_name_updated(new_first_name)

    @allure.feature("Редактирование профиля")
    @allure.story("Изменение ФИО пользователя")
    @allure.title("Смена middle name на {new_middle_name}")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("new_middle_name", [ProfileData.MIDDLE_NAME])
    def test_change_profile_middle_name(self, new_middle_name):
        with allure.step(f"Помещаем в текстовое поле значение {new_middle_name}"):
            self.my_info_page.update_middle_name_field(new_middle_name)

        with allure.step("Сохраняем изменения"):
            self.my_info_page.click_save_button()
            self.my_info_page.wait_for_spinner_to_disappear()

        with allure.step("Убеждаемся в том, что изменения применились"):
            self.my_info_page.is_middle_name_updated(new_middle_name)

    @allure.feature("Редактирование профиля")
    @allure.story("Изменение ФИО пользователя")
    @allure.title("Смена last name на {new_last_name}")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("new_last_name", [ProfileData.LAST_NAME])
    def test_change_profile_last_name(self, new_last_name):
        with allure.step(f"Помещаем в текстовое поле значение {new_last_name}"):
            self.my_info_page.update_last_name_field(new_last_name)

        with allure.step("Сохраняем изменения"):
            self.my_info_page.click_save_button()
            self.my_info_page.wait_for_spinner_to_disappear()

        with allure.step("Убеждаемся в том, что изменения применились"):
            self.my_info_page.is_last_name_updated(new_last_name)
