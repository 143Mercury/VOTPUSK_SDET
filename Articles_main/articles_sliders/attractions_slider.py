import time

from VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class AttractionLocators(BaseMethods):
    ATTRACTIONS_BLOCK_1 = (By.CSS_SELECTOR, '[class="landmarks__inner-item swiper-slide swiper-slide-active"]')
    ATTRACTIONS_BLOCK_2 = (By.CSS_SELECTOR, '[class="landmarks__inner-item swiper-slide swiper-slide-next"]')
    ATTRACTIONS_BLOCK_3 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[5]')
    ATTRACTIONS_BLOCK_4 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[6]')
    ATTRACTIONS_BLOCK_5 = (By.CSS_SELECTOR, '[class="landmarks__inner-item swiper-slide swiper-slide-active"]')
    ATTRACTIONS_BLOCK_6 = (By.CSS_SELECTOR, '[class="landmarks__inner-item swiper-slide swiper-slide-next"]')
    ATTRACTIONS_BLOCK_7 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[7]')
    ATTRACTIONS_BLOCK_8 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[8]')
    NAVIGATION_ARROW_PREV = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/button[1]')
    NAVIGATION_ARROW_NEXT = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/button[2]')
    READ_MORE_LINK_1 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[1]/div[2]/a[2]')
    READ_MORE_LINK_2 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[2]/div[2]/a[2]')
    READ_MORE_LINK_3 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[5]/div[2]/a[2]')
    READ_MORE_LINK_4 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[6]/div[2]/a[2]')
    READ_MORE_LINK_5 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[3]/div[2]/a[2]')
    READ_MORE_LINK_6 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[4]/div[2]/a[2]')
    READ_MORE_LINK_7 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[7]/div[2]/a[2]')
    READ_MORE_LINK_8 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[8]/div[2]/a[2]')
    COUNTRY_NAMED_1 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[1]/div[2]/a[3]')
    COUNTRY_NAMED_2 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[2]/div[2]/a[3]')
    COUNTRY_NAMED_3 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[5]/div[2]/a[3]')
    COUNTRY_NAMED_4 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[6]/div[2]/a[3]')
    COUNTRY_NAMED_5 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[3]/div[2]/a[3]')
    COUNTRY_NAMED_6 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[4]/div[2]/a[3]')
    COUNTRY_NAMED_7 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[7]/div[2]/a[3]')
    COUNTRY_NAMED_8 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[8]/div[2]/a[3]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_attractions_section(self):
        self.window_scroll_by(0, 2450)
        self.sleep(2)

    def click_to_prev_navigation_arrow(self):
        self.click_element(AttractionLocators.NAVIGATION_ARROW_PREV)

    def assert_attractions_blocks_1(self):
        self.is_visible(AttractionLocators.ATTRACTIONS_BLOCK_1)
        self.is_visible(AttractionLocators.READ_MORE_LINK_1)
        self.is_visible(AttractionLocators.COUNTRY_NAMED_1)
        self.sleep(2)

    def assert_attractions_blocks_2(self):
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_2)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_2)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_2)
        self.sleep(2)

    def assert_attractions_blocks_3(self):
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_3)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_3)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_3)
        self.sleep(2)

    def assert_attractions_blocks_4(self):
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_4)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_4)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_4)
        self.sleep(2)

    def assert_navigation_arrow_next(self):
        self.is_element_present(AttractionLocators.NAVIGATION_ARROW_NEXT)
        self.sleep(2)

    def double_click_to_navigation(self):
        self.double_click_element(AttractionLocators.NAVIGATION_ARROW_NEXT)
        self.sleep(2)

    def assert_attractions_blocks_5(self):
        self.is_element_present(AttractionLocators.READ_MORE_LINK_5)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_5)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_5)
        self.sleep(2)

    def assert_attractions_blocks_6(self):
        self.is_element_present(AttractionLocators.READ_MORE_LINK_6)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_6)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_6)
        self.sleep(2)

    def assert_attractions_blocks_7(self):
        self.is_element_present(AttractionLocators.READ_MORE_LINK_7)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_7)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_7)
        self.sleep(2)

    def assert_attractions_blocks_8(self):
        self.is_element_present(AttractionLocators.READ_MORE_LINK_8)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_8)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_8)
        self.sleep(2)
