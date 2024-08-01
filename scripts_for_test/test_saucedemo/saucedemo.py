from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service()
driver = webdriver.Chrome(service=service_object)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.refresh()
driver.set_page_load_timeout(30)
print(driver.get_window_size())
print(driver.get_window_position())
driver.find_element(By.NAME, "user-name").send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

print(driver.title)

driver.close()

driver.quit()