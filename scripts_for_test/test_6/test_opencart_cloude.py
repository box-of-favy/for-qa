from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--window-size=1920x1080")


def test_logo_presence():
    try:
        print("Initializing ChromeDriver...")
        service = Service() #executable_path=r'C:\Users\favy\Documents\work\opt\chromedriver.exe', port=9515
        driver = webdriver.Chrome(service=service, options=chrome_options)

        print("Opening webpage...")
        driver.get("http://localhost:8080/")

        print("Waiting for logo...")
        wait = WebDriverWait(driver, 10)
        logo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#logo a")))

        assert logo is not None, "Logo is not present"
        print("Test 1: Logo is present")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Waiting before quitting...")
        time.sleep(5)
        driver.quit()
        print("Browser closed.")


test_logo_presence()