"""
версия chatgpt
драйвера для браузеров есть в переменной среды
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
import logging
from urllib.parse import urlparse


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to use for tests: chrome, firefox, ie")
    parser.addoption("--base_url", action="store", default="http://localhost:8080", help="Base URL for Opencart")


@pytest.fixture
def browser(request, browser_name):
    driver = None
    browser_choice = request.config.getoption("--browser").lower()
    try:
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(service=ChromeService(), options=options)
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument("--start-maximized")
            driver = webdriver.Firefox(service=FirefoxService(), options=options)
        elif browser_name == "ie":
            options = webdriver.IeOptions()
            options.add_argument("--headless")
            options.add_argument("--start-maximized")
            driver = webdriver.Ie(service=IEService(), options=options)
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported.")

        logger.info(f"Started {browser_name} browser")
    except Exception as e:
        if driver:
            driver.quit()
        logger.error(f"Failed to start {browser_name} browser: {e}")
        raise e

    yield driver

    driver.quit()
    logger.info(f"Closed {browser_name} browser")


@pytest.fixture
def base_url(request):
    url = request.config.getoption("--base_url")
    result = urlparse(url)
    if not all([result.scheme, result.netloc]):
        raise ValueError(f"Invalid URL: {url}")
    return url

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")

"""
версия из урока, не полная
"""
# import pytest
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
#
# @pytest.fixture
# def driver(request):
#     # wd = webdriver.Firefox(firefox_binary="C:\\Program Files (x86)\\Nightly\\firefox.exe")
#     # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
#
#     capabilities = DesiredCapabilities.CHROME
#     # options = webdriver.ChromeOptions()
#     # options.add_argument("--headless")
#     # wd = webdriver.Chrome(options=options)
#     # wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
#
#     wd = webdriver.Chrome(r'C:\Users\favy\Documents\work\for-qa\venv')
#     print(wd.capabilities)
#     request.addfinalizer(wd.quit)
#     return wd
#

# def test_example(driver):
#     driver.get("https://otus.ru/")
#     assert driver.title() == "OTUS - Онлайн-образование"
