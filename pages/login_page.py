from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from pages.base_page import BasePage


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_INPUT_LOCATOR = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT_LOCATOR = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")

    ONLY_REQUIRED_SPAN_LOCATOR = (By.XPATH, "(//span[text()='Required'])[1]")
    BOTH_REQUIRED_SPAN_LOCATOR = (By.XPATH, "(//span[text()='Required'])[2]")

    INVALID_CREDENTIALS_DIV_LOCATOR = (By.XPATH, "//div[@role='alert']")

    def enter_username(self, username):
        username_input = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT_LOCATOR))
        username_input.send_keys(Keys.CONTROL + "A")
        username_input.send_keys(Keys.DELETE)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT_LOCATOR))
        password_input.send_keys(Keys.CONTROL + "A")
        password_input.send_keys(Keys.DELETE)
        password_input.send_keys(password)

    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON_LOCATOR)).click()

    def is_only_required_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.ONLY_REQUIRED_SPAN_LOCATOR))

    def is_both_required_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.BOTH_REQUIRED_SPAN_LOCATOR))

    def is_invalid_credentials_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.INVALID_CREDENTIALS_DIV_LOCATOR))

    def login_with(self, username, password):
        self.open_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit_button()
