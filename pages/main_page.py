from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class MainPage(Page):
    MAC = (By.CSS_SELECTOR, "a[href='https://gettop.us/product-category/macbook/']")

    def open_main_page(self):
        self.open_page()

    def hover_over_mac(self):
        actions = ActionChains(self.driver)
        mac = self.find_element(*self.MAC)
        actions.move_to_element(mac)
        actions.perform()
