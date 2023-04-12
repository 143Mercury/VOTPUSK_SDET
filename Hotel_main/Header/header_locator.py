from selenium.webdriver.common.by import By
from VOTPUSK.BaseMethods.object_methods import BaseMethods


class HeaderHotelLocator(BaseMethods):
    HOTEL_HEADER = (By.CSS_SELECTOR, '[class="header__container header__menu-container"]')
    HOTEL_TEXT_VISIBILITY = (By.XPATH, '//*[@id="page-header"]/section[1]/div[2]')
    HOTEL_TEXT_BANNER = (By.CSS_SELECTOR, '[class="hotels-banner__about"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_the_header(self):
        self.page_loaded(HeaderHotelLocator.HOTEL_HEADER)
        self.is_element_present(HeaderHotelLocator.HOTEL_HEADER)
        self.sleep(2)

    def check_the_text_visibility(self):
        self.page_loaded(HeaderHotelLocator.HOTEL_TEXT_VISIBILITY)
        self.is_element_present(HeaderHotelLocator.HOTEL_TEXT_VISIBILITY)
        self.sleep(2)

    def check_the_hotel_banner(self):
        self.page_loaded(HeaderHotelLocator.HOTEL_TEXT_BANNER)
        self.is_element_present(HeaderHotelLocator.HOTEL_TEXT_BANNER)
        self.sleep(2)

