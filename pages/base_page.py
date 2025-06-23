from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open_page(self):
        self.driver.get(self.PAGE_URL)

    def is_page_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))
