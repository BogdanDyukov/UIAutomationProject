from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from pages.base_page import BasePage


class MyInfoPage(BasePage):

    PAGE_URL = Links.MY_INFO_PAGE

    FIRST_NAME_INPUT_LOCATOR = (By.XPATH, "//input[@name='firstName']")
    MIDDLE_NAME_INPUT_LOCATOR = (By.XPATH, "//input[@name='middleName']")
    LAST_NAME_INPUT_LOCATOR = (By.XPATH, "//input[@name='lastName']")

    SAVE_BUTTON_LOCATOR = (By.XPATH, "(//button[@type='submit'])[1]")

    SPINNER_DIV_LOCATOR = (By.XPATH, "//div[@class='oxd-loading-spinner-container']")

    def update_text_field(self, locator, new_value):
        input_element = self.wait.until(EC.visibility_of_element_located(locator))
        input_element.send_keys(Keys.CONTROL + "A")
        input_element.send_keys(Keys.DELETE)
        input_element.send_keys(new_value)

    def update_first_name_field(self, new_first_name):
        self.update_text_field(self.FIRST_NAME_INPUT_LOCATOR, new_first_name)

    def update_middle_name_field(self, new_middle_name):
        self.update_text_field(self.MIDDLE_NAME_INPUT_LOCATOR, new_middle_name)

    def update_last_name_field(self, new_last_name):
        self.update_text_field(self.LAST_NAME_INPUT_LOCATOR, new_last_name)

    def wait_for_spinner_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER_DIV_LOCATOR))

    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON_LOCATOR)).click()

    def is_first_name_updated(self, expected_first_name):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_INPUT_LOCATOR, expected_first_name))

    def is_middle_name_updated(self, expected_middle_name):
        self.wait.until(EC.text_to_be_present_in_element_value(self.MIDDLE_NAME_INPUT_LOCATOR, expected_middle_name))

    def is_last_name_updated(self, expected_last_name):
        self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME_INPUT_LOCATOR, expected_last_name))
