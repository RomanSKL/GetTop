from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    PRO_13_LINK = (By.ID, 'menu-item-389')
    PRO_16_LINK = (By.ID, 'menu-item-380')
    PRO_AIR_LINK = (By.ID, 'menu-item-379')
    TEXT_PRO_16 = (By.CSS_SELECTOR, "h1[class='product-title product_title entry-title']")

    def click_pro_13(self):
        self.wait_for_element_click(*self.PRO_13_LINK)

    def click_pro_16(self):
        self.click(*self.PRO_16_LINK)

    def click_air(self):
        self.click(*self.PRO_AIR_LINK)

    def verify_pro_13_open(self):
        self.verify_url_contains_query('https://gettop.us/product/macbook-pro-13/')

    def verify_pro_16_open(self):
        self.verify_text('MacBook Pro 16-inch', *self.TEXT_PRO_16)

    def verify_air_open(self):
        self.verify_url_contains_query('https://gettop.us/product/macbook-air/')
