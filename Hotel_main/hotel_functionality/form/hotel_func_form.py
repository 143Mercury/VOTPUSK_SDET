import time

from selenium.webdriver.common.by import By
from VOTPUSK.BaseMethods.object_methods import BaseMethods
from VOTPUSK.Hotel_main.config.configuration import TestData


class HotelForm(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    HOTEL_FORM_VISIBLE = (By.CSS_SELECTOR, ' [class="hotels-search corner-radius-left"]')
    HOTEL_FORM_INPUT = (By.CSS_SELECTOR, '[class="hotels-search__item search-text"]')
    HOTEL_FORM_COLUM = (By.XPATH, '//*[@id="search-results"]/ul')
    FORM_TEXT_VISIBILITY = (By.XPATH, '//*[@id="search-hotels"]/label')
    HOTEL_CHECK_IN = (By.ID, 'h-checkin')
    CHECK_IN_TEXT = (By.XPATH, '//*[@id="reservation-form"]/div[2]/label')
    HOTEL_CHECK_OUT = (By.ID, 'h-checkout')
    CHECK_OUT_TEXT = (By.XPATH, '//*[@id="reservation-form"]/div[3]/label')
    HOTEL_ROOM_FOR = (By.CSS_SELECTOR, '[class="dropdown__btn hotels-search__item"]')
    HOTEL_DROPDOWN_PLUS = (By.CSS_SELECTOR, '[class="input-plus"]')
    HOTEL_DROPDOWN_MINUS = (By.CSS_SELECTOR, '[class="input-minus"]')
    HOTEL_QUANTITY_KIDS = (By.CSS_SELECTOR, '[class="collapse hotels-search__add-child"]')
    HOTEL_KIDS_COLUM = (By.CSS_SELECTOR, '[class="column"]')
    HOTEL_SEARCH_BUTTON = (By.XPATH, '//*[@id="reservation-form"]/input[4]')
    HOTEL_QUANTITY_TEXT = (By.XPATH, '//*[@id="reservation-form"]/div[4]/label')

    def check_the_total_hotel_form(self):
        self.is_element_present(HotelForm.HOTEL_FORM_VISIBLE)

    def check_hotel_form_input_and_text(self):
        self.is_element_present(HotelForm.HOTEL_FORM_INPUT)
        self.assert_elements_exist(HotelForm.FORM_TEXT_VISIBILITY)

    def hotel_input_city_and_click(self):
        self.send_keys_to_element(HotelForm.HOTEL_FORM_INPUT, TestData.CITY_INPUT_DATA)
        time.sleep(3)
        self.is_dropdown_present(HotelForm.HOTEL_FORM_COLUM)
        self.sleep(1)
        self.click_element(HotelForm.HOTEL_FORM_INPUT)

    def select_randomly_check_in_date(self):
        time.sleep(1)
        self.is_element_present(HotelForm.HOTEL_CHECK_IN)
        self.click_random_enabled_day_in_calendar(HotelForm.HOTEL_CHECK_IN)
        self.is_visible(HotelForm.CHECK_IN_TEXT)

    def select_randomly_check_out_date(self):
        time.sleep(1)
        self.is_element_present(HotelForm.HOTEL_CHECK_OUT)
        self.click_random_enabled_day_in_calendar(HotelForm.HOTEL_CHECK_OUT)
        self.is_visible(HotelForm.CHECK_OUT_TEXT)

    def check_dropdown_quantity(self):
        self.is_element_present(HotelForm.HOTEL_ROOM_FOR)
        self.click_element(HotelForm.HOTEL_ROOM_FOR)
        self.is_element_present(HotelForm.HOTEL_ROOM_FOR)

    def select_randomly_quantity(self):
        self.is_visible(HotelForm.HOTEL_DROPDOWN_PLUS)
        self.do_randint_click(HotelForm.HOTEL_DROPDOWN_PLUS)
        self.is_element_present(HotelForm.HOTEL_DROPDOWN_MINUS)

    def select_randomly_kids_quantity(self):
        self.is_visible(HotelForm.HOTEL_QUANTITY_TEXT)
        time.sleep(1)
        self.click_element(HotelForm.HOTEL_QUANTITY_KIDS)
        self.assert_element_visibility(HotelForm.HOTEL_KIDS_COLUM)

    def check_the_search_button(self):
        time.sleep(1)
        self.assert_element_to_be_clickable(HotelForm.HOTEL_SEARCH_BUTTON)