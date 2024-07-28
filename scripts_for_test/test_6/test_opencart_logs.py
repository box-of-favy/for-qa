from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_logs():
    # Настройка опций для headless режима
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Обычно рекомендуется для headless режима
    chrome_options.add_argument("--window-size=1920x1080")  # Установка размера окна

    # Инициализация веб-драйвера с опциями
    driver = webdriver.Chrome(options=chrome_options)

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

    # Закрытие драйвера
    driver.quit()
    print("Closed the browser")

# Тестовая функция для pytest
def test_logs_wrapper():
    test_logs()
