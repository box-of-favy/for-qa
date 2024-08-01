import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def open_driver():
    # Настройка опций для headless режима
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Обычно рекомендуется для headless режима
    chrome_options.add_argument("--window-size=1920x1080")  # Установка размера окна

    # Инициализация веб-драйвера с опциями
    driver = webdriver.Chrome(options=Options())

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

# Тест 1: Проверка наличия логотипа
def test_logo_presence(driver):
    logo = driver.find_element(By.ID, "logo")
    assert logo is not None, "Logo is not present"
    
# Тест 2: Проверка поиска товаров
def test_search(driver):
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("MacBook" + Keys.RETURN)
    search_results = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    assert len(search_results) > 0, "Search results are empty"
    
# Тест 3: Проверка наличия элементов в верхнем меню
def test_top_menu(driver):
    top_menu_items = driver.find_elements(By.CSS_SELECTOR, "#top-links ul li")
    assert len(top_menu_items) >= 5, "Top menu items are less than expected"

# Тест 4: Проверка добавления товара в корзину
def test_add_to_cart(driver):
    first_product_add_button = driver.find_element(By.CSS_SELECTOR,
                                                   ".product-thumb .button-group button[onclick*='cart.add']")
    first_product_add_button.click()

    # Явное ожидание изменения текста элемента
    cart_total = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart-total"), "1 item(s)")
    )
    assert cart_total, "Item not added to cart"

# Тест 5: Проверка наличия промоблока (слайдера)
def test_promo_block(driver):
    swiper = driver.find_element(By.ID, "content")
    assert swiper is not None, "Swiper is not present"



