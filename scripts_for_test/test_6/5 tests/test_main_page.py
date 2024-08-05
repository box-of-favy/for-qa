from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.MainPage import MainPageLocators, TopPanelLocators, MenuLocators, SlideshowLocators, FooterLocators
 
# Тест 1: Проверка наличия логотипа
def test_logo_presence(driver):
    logo = driver.find_element(*MainPageLocators.LOGO)
    assert logo is not None, "Logo is not present"

# Тест 2: Проверка кнопки логотипа
def test_logo_click(driver):
    driver.get('http://localhost:8080/index.php?route=account/login')
    logo = driver.find_element(*MainPageLocators.LOGO)
    logo.click()
    assert driver.current_url == "http://localhost:8080/index.php?route=common/home", "Logo does not lead to main page"

def test_top_panel(driver):
    # Проверка наличия верхней панели
    top_panel = driver.find_element(*TopPanelLocators.TOP_PANEL)
    assert top_panel is not None, "Top panel is not present"

def test_elements(driver):
    # Проверка наличия элементов верхней панели
    elements = {
        "Currency": TopPanelLocators.CURRENCY,
        "My Account": TopPanelLocators.MY_ACCOUNT,
        "Wish List (0)": TopPanelLocators.WISH_LIST,
        "Shopping Cart": TopPanelLocators.SHOPPING_CART,
        "Checkout": TopPanelLocators.CHECKOUT
    }

    for name, locator in elements.items():
        element = driver.find_element(*locator)
        assert element is not None, f"{name} is not present"


def test_currency_dropdown(driver):
    # Проверка наличия выпадающего списка для Currency
    driver.find_element(*TopPanelLocators.CURRENCY).click()
    dropdown = driver.find_element(*TopPanelLocators.CURRENCY_DROPDOWN)
    assert dropdown is not None, "Currency dropdown is not present"

    for name, locator in TopPanelLocators.CURRENCY_ITEMS.items():
        item = dropdown.find_element(*locator)
        assert item is not None, f"{name} in Currency dropdown is not present"
def test_my_account_dropdown(driver):
    # Проверка наличия выпадающего списка для My Account
    driver.find_element(*TopPanelLocators.MY_ACCOUNT).click()
    dropdown = driver.find_element(*TopPanelLocators.MY_ACCOUNT_DROPDOWN)
    assert dropdown is not None, "My Account dropdown is not present"

    for name, locator in TopPanelLocators.MY_ACCOUNT_ITEMS.items():
        item = dropdown.find_element(*locator)
        assert item is not None, f"{name} in My Account dropdown is not present"

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
    slideshow = driver.find_element(*SlideshowLocators.SLIDESHOW)
    assert slideshow is not None, "Slideshow is not present"

def test_footer(driver):
    # Проверка наличия элементов в футере, где FooterLocators это класс в locators, footer_sections это словарь
    for name, locator in FooterLocators.FOOTER_SECTIONS.items():
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        assert element is not None, f"{name} is not present"

