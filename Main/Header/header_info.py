from VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class HeaderLocators(BaseMethods):
    HEADER_INFO = (By.CSS_SELECTOR, '[class="header__info"]')
    BURGER_MENU = (By.CSS_SELECTOR, '[class="header__burger burger"]')
    LOGO_ICON = (By.CSS_SELECTOR, '[class="header__logo-icon"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def header_info(self):
        self.page_loaded(HeaderLocators.HEADER_INFO)
        self.is_element_present(HeaderLocators.HEADER_INFO)

    def burger_menu(self):
        self.page_loaded(HeaderLocators.BURGER_MENU)
        self.is_element_present(HeaderLocators.BURGER_MENU)

    def logo_info(self):
        self.page_loaded(HeaderLocators.LOGO_ICON)
        self.is_element_present(HeaderLocators.LOGO_ICON)
