import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("test_log.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

# Настройка опций для headless режима
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  # Обычно рекомендуется для headless режима
chrome_options.add_argument("--window-size=1920x1080")  # Установка размера окна

# Инициализация веб-драйвера с опциями
driver = webdriver.Chrome(options=chrome_options)

# Открытие главной страницы
# driver.get("http://localhost:8080/")

# Открытие главной страницы

host = "localhost"
port = 8080
url = f"http://{host}:{port}/"
logger.info(f"Attempting to open URL: {url} with host: {host} and port: {port}")
try:
    driver.get(url)
    logger.info(f"Successfully opened URL: {url} with host: {host} and port: {port}")
except Exception as e:
    logger.error(f"Failed to open URL: {url} with host: {host} and port: {port}, Error: {e}")




# Тест 1: Проверка наличия логотипа
def test_logo_presence():
    logo = driver.find_element(By.CSS_SELECTOR, "#logo a")
    assert logo is not None, "Logo is not present"
    print("Test 1: Logo is present")

# Закрытие драйвера
driver.quit()

#
# # Тест 2: Проверка поиска товаров
# def test_search():
#     search_box = driver.find_element(By.NAME, "search")
#     search_box.send_keys("MacBook" + Keys.RETURN)
#     search_results = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
#     assert len(search_results) > 0, "Search results are empty"
#     print("Test 2: Search function is working")
#
#
# # Тест 3: Проверка наличия элементов в верхнем меню
# def test_top_menu():
#     top_menu_items = driver.find_elements(By.CSS_SELECTOR, "#top-links ul li")
#     assert len(top_menu_items) >= 5, "Top menu items are less than expected"
#     print("Test 3: Top menu items are present")
#
#
# # Тест 4: Проверка добавления товара в корзину
# def test_add_to_cart():
#     first_product_add_button = driver.find_element(By.CSS_SELECTOR,
#                                                    ".product-thumb .button-group button[onclick*='cart.add']")
#     first_product_add_button.click()
#
#     # Явное ожидание изменения текста элемента
#     cart_total = WebDriverWait(driver, 10).until(
#         EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart-total"), "1 item(s)")
#     )
#     assert cart_total, "Item not added to cart"
#     print("Test 4: Item added to cart")


# Тест 5: Проверка наличия промоблока (слайдера)

# def test_promo_block():
#     try:
#         # Явное ожидание появления элемента
#         promo_block = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "#slideshow0"))
#         )
#         assert promo_block is not None, "Promo block is not present"
#         print("Test 5: Promo block is present")
#
#         # Проверка наличия слайдов
#         slides = promo_block.find_elements(By.CSS_SELECTOR, ".swiper-slide")
#         num_slides = len(slides)
#         print(f"Found {num_slides} states in the slideshow.")
#
#         # Вывод информации о каждом слайде
#         for i, slide in enumerate(slides, start=1):
#             slide_text = slide.text if slide.text else "No text"
#             slide_image = slide.find_element(By.TAG_NAME, "img").get_attribute("src")
#             print(f"State {i}: Text = '{slide_text}', Image URL = '{slide_image}'")
#
#     except Exception as e:
#         print(f"Promo block not found: {e}")

# Тест 5: Проверка наличия промоблока (слайдера)
# def test_promo_block():
#     promo_block = driver.find_element(By.CSS_SELECTOR, "#slideshow0")
#     # logo = driver.find_element(By.CSS_SELECTOR, "#logo a")
#     assert promo_block is not None, "Promo block is not present"
#     print("Test 5: Promo block is present")


# Выполнение тестов
# test_logo_presence()
# test_search()
# test_top_menu()
# test_add_to_cart()
# test_promo_block()

# # Закрытие драйвера
# driver.quit()
