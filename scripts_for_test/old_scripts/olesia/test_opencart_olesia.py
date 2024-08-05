from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_driver():
    # Настройка опций для headless режима
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Обычно рекомендуется для headless режима
    chrome_options.add_argument("--window-size=1920x1080")  # Установка размера окна

    # Инициализация веб-драйвера с опциями
    return webdriver.Chrome(options=chrome_options)


def close_driver(driver):
    # Закрытие драйвера
    driver.quit()
    print("Closed the browser")


def test_logs():
    driver = open_driver()

    # Открытие главной страницы
    host = "localhost"
    port = 8080
    url = f"http://{host}:{port}/"
    print(f"Attempting to open URL: {url} with host: {host} and port: {port}")
    try:
        driver.get(url)
        print(f"Successfully opened URL: {url} with host: {host} and port: {port}")
    except Exception as e:
        print(f"Failed to open URL: {url} with host: {host} and port: {port}, Error: {e}")

    close_driver(driver)


def test_logo_present():
    driver = open_driver()
    driver.get("http://localhost:8080")
    wait = WebDriverWait(driver, 10)
    logo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#logo a")))
    try:
        assert logo is not None, "Logo is not present"
        print(f"Logo is present")
    except Exception as e:
        print(f"Logo is not present, Error: {e}")
    close_driver(driver)
