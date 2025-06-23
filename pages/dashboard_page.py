from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from pages.base_page import BasePage


class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_REF_LOCATOR = (By.XPATH, "//a[@href='/web/index.php/pim/viewMyDetails']")
    DASHBOARD_HEADER_LOCATOR = (By.XPATH, "//h6[text()='Dashboard']")

    def click_my_info_ref(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_REF_LOCATOR)).click()

    def expect_dashboard_header(self):
        self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER_LOCATOR))