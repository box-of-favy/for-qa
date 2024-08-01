from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест 1: Проверка наличия логотипа
def test_logo_presence(driver):
    logo = driver.find_element(By.CSS_SELECTOR, "#logo")
    assert logo is not None, "Logo is not present"

# Тест 2: Проверка кнопки логотипа
def test_logo_click(driver):
    driver.get('http://localhost:8080/index.php?route=account/login')
    logo = driver.find_element(By.CSS_SELECTOR, "#logo a")
    logo.click()
    assert driver.current_url == "http://localhost:8080/index.php?route=common/home", "Logo does not lead to main page"

def test_top_panel(driver):
    # Проверка наличия верхней панели
    top_panel = driver.find_element(By.CSS_SELECTOR, 'nav#top')
    assert top_panel is not None, "Top panel is not present"

def test_elements(driver):
    # Проверка наличия элементов верхней панели
    elements = {
        "Currency": 'form#form-currency button.dropdown-toggle',
        "My Account": 'a[title="My Account"]',
        "Wish List (0)": 'a#wishlist-total',
        "Shopping Cart": 'a[title="Shopping Cart"]',
        "Checkout": 'a[title="Checkout"]'
    }

    for name, selector in elements.items():
        element = driver.find_element(By.CSS_SELECTOR, selector)
        assert element is not None, f"{name} is not present"


def test_currency_dropdown(driver):
    # Проверка наличия выпадающего списка для Currency
    driver.find_element(By.CSS_SELECTOR, 'form#form-currency button.dropdown-toggle').click()
    dropdown = driver.find_element(By.CSS_SELECTOR, 'form#form-currency ul.dropdown-menu')
    assert dropdown is not None, "Currency dropdown is not present"

    items = ['button[name="EUR"]', 'button[name="GBP"]', 'button[name="USD"]']
    for item_selector in items:
        item = dropdown.find_element(By.CSS_SELECTOR, item_selector)
        assert item is not None, f"{item_selector} in Currency dropdown is not present"
def test_my_account_dropdown(driver):
    # Проверка наличия выпадающего списка для My Account
    driver.find_element(By.CSS_SELECTOR, 'a[title="My Account"]').click()
    dropdown = driver.find_element(By.CSS_SELECTOR, 'ul.dropdown-menu-right')
    assert dropdown is not None, "My Account dropdown is not present"

    items = ['a[href*="account/register"]', 'a[href*="account/login"]']
    for item_selector in items:
        item = dropdown.find_element(By.CSS_SELECTOR, item_selector)
        assert item is not None, f"{item_selector} in My Account dropdown is not present"

def test_menu_elements(driver):
    # Проверка наличия элементов в меню навигации
    menu_elements = {
        "Desktops": 'a[href*="product/category&path=20"]',
        "Laptops & Notebooks": 'a[href*="product/category&path=18"]',
        "Components": 'a[href*="product/category&path=25"]',
        "Tablets": 'a[href*="product/category&path=57"]',
        "Software": 'a[href*="product/category&path=17"]',
        "Phones & PDAs": 'a[href*="product/category&path=24"]',
        "Cameras": 'a[href*="product/category&path=33"]',
        "MP3 Players": 'a[href*="product/category&path=34"]'
    }

    for name, selector in menu_elements.items():
        element = driver.find_element(By.CSS_SELECTOR, selector)
        assert element is not None, f"{name} is not present"


def test_slideshow_presence(driver):
    # Проверка наличия слайдера
    slideshow = driver.find_element(By.CSS_SELECTOR, 'div#slideshow0')
    assert slideshow is not None, "Slideshow is not present"\

def test_menu_elements(driver):
    # Проверка наличия элементов в меню навигации
    menu_elements = {
        "Desktops": 'a[href*="product/category&path=20"]',
        "Laptops & Notebooks": 'a[href*="product/category&path=18"]',
        "Components": 'a[href*="product/category&path=25"]',
        "Tablets": 'a[href*="product/category&path=57"]',
        "Software": 'a[href*="product/category&path=17"]',
        "Phones & PDAs": 'a[href*="product/category&path=24"]',
        "Cameras": 'a[href*="product/category&path=33"]',
        "MP3 Players": 'a[href*="product/category&path=34"]'
    }

    for name, selector in menu_elements.items():
        element = driver.find_element(By.CSS_SELECTOR, selector)
        assert element is not None, f"{name} is not present"

def test_footer(driver):
    # Проверка наличия элементов в футере
    footer_elements = {
        "Information": "//footer//h5[text()='Information']",
        "Customer Service": "//footer//h5[text()='Customer Service']",
        "Extras": "//footer//h5[text()='Extras']",
        "My Account": "//footer//h5[text()='My Account']",
    }

    for name, selector in footer_elements.items():
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, selector))
        )
        assert element is not None, f"{name} is not present"

