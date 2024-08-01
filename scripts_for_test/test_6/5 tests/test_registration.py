from selenium.webdriver.common.by import By

def test_my_account(driver):

    # Нажатие на "My Account"
    my_account = driver.find_element(By.XPATH, '//a[@title="My Account"]')
    my_account.click()

def test_dropdown(driver):
    # Ожидание появления выпадающего списка
    dropdown_menu = driver.find_element(By.CLASS_NAME, 'dropdown-menu.dropdown-menu-right')

    # Проверка наличия элементов "Register" и "Login" в выпадающем списке
    register_link = dropdown_menu.find_element(By.LINK_TEXT, 'Register')
    login_link = dropdown_menu.find_element(By.LINK_TEXT, 'Login')

    assert register_link is not None, "Register link is not present in the dropdown menu"
    assert login_link is not None, "Login link is not present in the dropdown menu"

def test_register(driver):
    # Нажатие на "Register"
    register = driver.find_element(By.XPATH, '//a[text()="Register"]')
    register.click()
def test_input(driver, user_email, user_password):
    # Ввод данных
    driver.find_element(By.ID, 'input-firstname').send_keys('John')
    driver.find_element(By.ID, 'input-lastname').send_keys('Doe')
    driver.find_element(By.ID, 'input-email').send_keys(user_email) #задан фикстурой в conftest
    driver.find_element(By.ID, 'input-telephone').send_keys('1234567890')
    driver.find_element(By.ID, 'input-password').send_keys(user_password) #задан фикстурой в conftest
    driver.find_element(By.ID, 'input-confirm').send_keys(user_password) #задан фикстурой в conftest

    # Чекбокс для согласия с политикой конфиденциальности
    privacy_checkbox = driver.find_element(By.NAME, 'agree')
    privacy_checkbox.click()

    # Отправка формы
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary')
    submit_button.click()

    # Проверка успешной регистрации
    assert "Congratulations! Your new account has been successfully created!" in driver.page_source, "Не зарегистрировать аккаунт"
    assert "route=account/success" in driver.current_url, "Не зарегистрировать аккаунт"

def test_logout(driver, user_email, user_password):

    my_account = driver.find_element(By.XPATH, '//a[@title="My Account"]')
    my_account.click()
    logout_link = driver.find_element(By.XPATH, "//a[text()='Logout']")
    logout_link.click()

    # Проверка успешного выхода
    assert "route=account/logout" in driver.current_url, "Не удалось выйти из аккаунта"

def test_login(driver):

    my_account = driver.find_element(By.XPATH, '//a[@title="My Account"]')
    my_account.click()
    login = driver.find_element(By.XPATH, '//a[text()="Login"]')
    login.click()
    assert "route=account/login" in driver.current_url, "Не удалось войти в аккаунт"

