"""
версия chatgpt
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to use for tests: chrome, firefox, ie")
    parser.addoption("--base_url", action="store", default="http://localhost:8080", help="Base URL for Opencart")


@pytest.fixture
def browser(request):
    browser_choice = request.config.getoption("--browser").lower()

    if browser_choice == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(executable_path=r'C:\Users\favy\Documents\work\for-qa\venv\chromedriver.exe'), options=options)
    elif browser_choice == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(service=FirefoxService(executable_path=r'C:\Users\favy\Documents\work\for-qa\venv\geckodriver.exe'), options=options)
    elif browser_choice == "ie":
        options = webdriver.IeOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Ie(service=IEService(executable_path=r'C:\Users\favy\Documents\work\for-qa\venv\IEDriverServer.exe'), options=options)
    else:
        raise ValueError(f"Browser '{browser_choice}' is not supported.")

    yield driver  # Точка, где выполнение передается тесту. После завершения теста выполнение продолжится ниже

    driver.quit()  # Этот код выполняется после завершения теста, закрывая браузер


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
