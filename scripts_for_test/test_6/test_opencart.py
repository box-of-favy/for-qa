from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Настройка опций для headless режима
chrome_options = Options()
chrome_options.add_argument("--headless")  # Включение headless режима
chrome_options.add_argument("--disable-gpu")  # Отключение GPU, рекомендуется для headless режима
chrome_options.add_argument("--window-size=1920x1080")  # Установка размера окна

# Инициализация веб-драйвера с опциями
driver = webdriver.Chrome(options=chrome_options)

# Открытие главной страницы
driver.get("http://localhost:8080/")

# Тест 1: Проверка наличия логотипа
def test_logo_presence():
    logo = driver.find_element(By.CSS_SELECTOR, "#logo")
    assert logo is not None, "Logo is not present"
    print("Test 1: Logo is present")

# Выполнение тестов
test_logo_presence()

# Закрытие драйвера
driver.quit()