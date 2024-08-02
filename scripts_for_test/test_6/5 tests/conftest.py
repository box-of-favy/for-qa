import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.edge.options import Options as EdgeOptions
from faker import Faker


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def browser_name(request):
    return request.param
def open_driver(browser):
    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
    # elif browser == "edge":
    #     options = EdgeOptions()
    #     options.add_argument("--start-maximized")
    #     # options.add_argument("--headless")
    #     driver = webdriver.Edge(options=options)
    elif browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Открываем тестовую страницу
    driver.get("http://localhost:8080/")

    return driver

def close_driver(driver):
    # Закрытие драйвера
    driver.quit()

@pytest.fixture(scope="session")
def driver(browser_name):
    driver = open_driver(browser_name)
    yield driver
    close_driver(driver)

@pytest.fixture(scope="session")
def user_email():
    return Faker().email()

@pytest.fixture(scope="session")
def user_password():
    return Faker().password()