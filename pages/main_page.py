from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    DEALS = (By.CSS_SELECTOR, "div.mega-menu")

    def open_main(self):
        self.open_url("https://www.amazon.com/")

    def open_new_arrivals(self):
        self.open_url("https://www.amazon.com/gp/product/B074TBCSC8")

    def verify_deals_present(self):
        self.wait_for_element_appear(*self.DEALS)
