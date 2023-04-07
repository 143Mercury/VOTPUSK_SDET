from VOTPUSK_SDET.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class HeaderLocators(BaseMethods):
    HEADER_INFO = (By.CSS_SELECTOR, '[class="header__info"]')
    BURGER_MENU = (By.CSS_SELECTOR, '[class="header__burger burger"]')
    LOGO_ICON = (By.CSS_SELECTOR, '[class="header__logo-icon"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def header_info(self):
        header_info = self.assert_element_visibility(HeaderLocators.HEADER_INFO)
        return header_info

    def burger_menu(self):
        burger_menu = self.assert_element_visibility(HeaderLocators.BURGER_MENU)
        return burger_menu

    def logo_info(self):
        logo_info = self.assert_element_visibility(HeaderLocators.LOGO_ICON)
        return logo_info
