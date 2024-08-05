# MainPage.py

from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.CSS_SELECTOR, "#logo a")
    SEARCH_BOX = (By.CSS_SELECTOR, 'input[name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-default.btn-lg')
    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, 'div#content h1')
    PRODUCT_THUMB = (By.CSS_SELECTOR, 'div.product-thumb')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h4 a')


class TopPanelLocators:
    TOP_PANEL = (By.CSS_SELECTOR, 'nav#top')
    CURRENCY = (By.CSS_SELECTOR, 'form#form-currency button.dropdown-toggle')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, 'form#form-currency ul.dropdown-menu')
    CURRENCY_ITEMS = {
        "EUR": (By.CSS_SELECTOR, 'button[name="EUR"]'),
        "GBP": (By.CSS_SELECTOR, 'button[name="GBP"]'),
        "USD": (By.CSS_SELECTOR, 'button[name="USD"]')
    }
    MY_ACCOUNT = (By.CSS_SELECTOR, 'a[title="My Account"]')
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, 'ul.dropdown-menu-right')
    MY_ACCOUNT_ITEMS = {
        "Register": (By.CSS_SELECTOR, 'a[href*="account/register"]'),
        "Login": (By.CSS_SELECTOR, 'a[href*="account/login"]')
    }
    WISH_LIST = (By.CSS_SELECTOR, 'a#wishlist-total')
    SHOPPING_CART = (By.CSS_SELECTOR, 'a[title="Shopping Cart"]')
    CHECKOUT = (By.CSS_SELECTOR, 'a[title="Checkout"]')


class MenuLocators:
    DESKTOPS = (By.CSS_SELECTOR, 'a[href*="product/category&path=20"]')
    LAPTOPS_NOTEBOOKS = (By.CSS_SELECTOR, 'a[href*="product/category&path=18"]')
    COMPONENTS = (By.CSS_SELECTOR, 'a[href*="product/category&path=25"]')
    TABLETS = (By.CSS_SELECTOR, 'a[href*="product/category&path=57"]')
    SOFTWARE = (By.CSS_SELECTOR, 'a[href*="product/category&path=17"]')
    PHONES_PDAS = (By.CSS_SELECTOR, 'a[href*="product/category&path=24"]')
    CAMERAS = (By.CSS_SELECTOR, 'a[href*="product/category&path=33"]')
    MP3_PLAYERS = (By.CSS_SELECTOR, 'a[href*="product/category&path=34"]')


class SlideshowLocators:
    SLIDESHOW = (By.CSS_SELECTOR, 'div#slideshow0')


class FooterLocators:
    FOOTER_SECTIONS = {
        "Information": (By.XPATH, "//footer//h5[text()='Information']"),
        "Customer Service": (By.XPATH, "//footer//h5[text()='Customer Service']"),
        "Extras": (By.XPATH, "//footer//h5[text()='Extras']"),
        "My Account": (By.XPATH, "//footer//h5[text()='My Account']")
    }
