# # pages.py
#
# from locators import MainPageLocators, TopPanelLocators
#
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#
# class MainPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def is_logo_present(self):
#         return self.driver.find_element(*MainPageLocators.LOGO) is not None
#
#     def click_logo(self):
#         self.driver.find_element(*MainPageLocators.LOGO).click()
#
#     def search_for(self, text):
#         search_box = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
#         search_box.clear()
#         search_box.send_keys(text)
#         self.driver.find_element(*MainPageLocators.SEARCH_BUTTON).click()
#
#     def is_search_results_header_present(self):
#         return self.driver.find_element(*MainPageLocators.SEARCH_RESULTS_HEADER) is not None
#
#     def get_search_results_header_text(self):
#         return self.driver.find_element(*MainPageLocators.SEARCH_RESULTS_HEADER).text
#
#     def is_product_present(self):
#         return self.driver.find_element(*MainPageLocators.PRODUCT_THUMB) is not None
#
#     def get_product_name(self):
#         return self.driver.find_element(*MainPageLocators.PRODUCT_NAME).text
#
# class TopPanel(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def are_top_panel_elements_present(self):
#         elements = [
#             TopPanelLocators.CURRENCY,
#             TopPanelLocators.MY_ACCOUNT,
#             TopPanelLocators.WISH_LIST,
#             TopPanelLocators.SHOPPING_CART,
#             TopPanelLocators.CHECKOUT
#         ]
#         for locator in elements:
#             if not self.driver.find_element(*locator):
#                 return False
#         return True
