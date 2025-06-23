import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


@pytest.fixture(scope="class")
def driver_class_scope():
    driver = create_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_function_scope():
    driver = create_driver()
    yield driver
    driver.quit()
