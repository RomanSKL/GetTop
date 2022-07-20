from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class MainPage(Page):
    MAC = (By.ID, 'menu-item-468')
    CLICK_RIGHT_ARROW = (By.CSS_SELECTOR, "button[class='flickity-button flickity-prev-next-button next']")
    CLICK_LEFT_ARROW = (By.CSS_SELECTOR, "button[class='flickity-button flickity-prev-next-button previous']")
    CLICK_RIGHT_DOTT = (By.CSS_SELECTOR, "li[aria-label='Page dot 2']")
    CLICK_LEFT_DOTT = (By.CSS_SELECTOR, "li[aria-label='Page dot 1']")
    CLICK_BANNER1 = (By.CSS_SELECTOR, "a[href='/product-category/ipad/']")
    CLICK_BANNER2 = (By.CSS_SELECTOR, "a[href='/product-category/macbook/']")
    BANNER1 = (By.CSS_SELECTOR, "a[href='/product-category/ipad/']")

    def open_main_page(self):
        self.open_page()

    def hover_over_mac(self):
        actions = ActionChains(self.driver)
        mac = self.wait_for_element_appear(*self.MAC)
        actions.move_to_element(mac)
        actions.perform()

    def hover_over_banner1(self):
        actions = ActionChains(self.driver)
        banner1 = self.find_element(*self.BANNER1)
        actions.move_to_element(banner1)
        actions.perform()

    def click_right_arrow(self):
        self.wait_for_element_click(*self.CLICK_RIGHT_ARROW)

    def click_left_arrow(self):
        self.wait_for_element_click(*self.CLICK_LEFT_ARROW)

    def click_right_dott(self):
        self.wait_for_element_click(*self.CLICK_RIGHT_DOTT)

    def click_left_dott(self):
        self.wait_for_element_click(*self.CLICK_LEFT_DOTT)

    def click_banner1(self):
        self.wait_for_element_click(*self.CLICK_BANNER1)

    def click_banner2(self):
        self.wait_for_element_click(*self.CLICK_BANNER2)

    def click_banner1_page_opened(self):
        self.verify_url_contains_query('https://gettop.us/product-category/ipad/')

    def click_banner2_page_opened(self):
        self.verify_url_contains_query('https://gettop.us/product-category/macbook/')
