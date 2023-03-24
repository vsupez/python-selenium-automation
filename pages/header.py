from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURNS_ORDERS = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')
    CART_COUNT = (By.ID, 'nav-cart-count')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, 'a[href="#switch-lang=es_US"]')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    NEW_ARR = (By.CSS_SELECTOR, "#nav-subnav a[aria-label='New Arrivals']")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_ReturnsAndOrders(self):
        self.wait_for_element_click(*self.RETURNS_ORDERS)


    def click_cart_icon(self):
        self.click(*self.CART_ICON)


    def verify_cart_count(self,expected_count):
        self.verify_text(expected_count, *self.CART_COUNT)

    def hover_lang_options(self):
        lang_options = self.driver.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_lang_shown(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self, alias):
        department_dd = self.driver.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value(f'search-alias={alias}')

    def hover_new_arrivals(self):
        new_arrivals = self.driver.find_element(*self.NEW_ARR)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

