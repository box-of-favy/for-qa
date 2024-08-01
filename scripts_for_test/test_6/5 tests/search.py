from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_functionality(driver):
    # Ожидание загрузки строки поиска
    search_box = driver.find_element(By.CSS_SELECTOR, 'input[name="search"]')
    assert search_box is not None, "Search box is not present"

    # Ввод текста "HP LP3065" в строку поиска
    search_box.send_keys("HP LP3065")

    # Нажатие на кнопку поиска
    search_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-default.btn-lg')
    search_button.click()

def test_results(driver):
    # Ожидание загрузки результатов поиска
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="search"]'))
    )
    assert results is not None, "Search results page did not load"

    # Дополнительная проверка наличия продукта HP LP3065 в результатах поиска
    product = driver.find_element(By.CSS_SELECTOR, 'div.product-thumb')
    product_name = product.find_element(By.CSS_SELECTOR, 'h4 a')
    assert product_name.text == "HP LP3065", "Product 'HP LP3065' is not found in the search results"

    print(" Поиск прошел успешно и продукт найден в результатах.")
