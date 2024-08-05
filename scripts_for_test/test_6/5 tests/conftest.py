# claude оба браузера по очереди, но можно выбрать браузер
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from faker import Faker


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="both",
                     help="Browser to use for tests: chrome, firefox, or both")


def pytest_generate_tests(metafunc):
    if "driver" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("browser")
        if browsers == "both":
            metafunc.parametrize("browser", ["chrome", "firefox"], scope="module")
        else:
            metafunc.parametrize("browser", [browsers], scope="module")


def open_driver(browser):
    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
    elif browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("http://localhost:8080/")
    return driver


@pytest.fixture(scope="module")
def driver(browser):
    driver = open_driver(browser)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def user_email():
    return Faker().email()


@pytest.fixture(scope="function")
def user_password():
    return Faker().password()
