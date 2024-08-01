import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker

def open_driver():
    # Настройка опций для headless режима
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Обычно рекомендуется для headless режима
    chrome_options.add_argument("--window-size=1920x1080")  # Установка размера окна

    # Инициализация веб-драйвера с опциями
    driver = webdriver.Chrome(options=chrome_options)

    # Открываем тестовую страницу
    driver.get("http://localhost:8080/")

    return driver

def close_driver(driver):
    # Закрытие драйвера
    driver.quit()

@pytest.fixture(scope="session")
def driver():
    driver = open_driver()
    yield driver
    close_driver(driver)

@pytest.fixture(scope="session")
def user_email():
    return Faker().email()

@pytest.fixture(scope="session")
def user_password():
    return Faker().password()