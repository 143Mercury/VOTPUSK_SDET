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

    def check_the_main_hotel_form(self):
        self.page_loaded(HotelForm.HOTEL_FORM_VISIBLE)
        self.is_element_present(HotelForm.HOTEL_FORM_VISIBLE)
        self.sleep(2)

    def wait_until_page_load_and_assert_elements(self):
        self.page_loaded(HotelForm.HOTEL_FORM_INPUT)
        self.is_element_present(HotelForm.HOTEL_FORM_INPUT)
        self.sleep(2)

    def send_keys_to_hotel_form(self):
        self.page_loaded(HotelForm.HOTEL_FORM_INPUT)
        self.send_keys_to_element(HotelForm.HOTEL_FORM_INPUT, TestData.CITY_INPUT_DATA)
        self.sleep(2)

    def assert_hotel_dropdown_present(self):
        self.is_dropdown_present(HotelForm.HOTEL_FORM_COLUM)
        self.sleep(2)

    def select_randomly_check_in_date(self):
        self.page_loaded(HotelForm.HOTEL_CHECK_IN)
        self.is_element_present(HotelForm.HOTEL_CHECK_IN)
        self.click_random_enabled_day_in_calendar(HotelForm.HOTEL_CHECK_IN)
        self.sleep(2)

    def select_randomly_check_out_date(self):
        self.page_loaded(HotelForm.HOTEL_CHECK_OUT)
        self.is_element_present(HotelForm.HOTEL_CHECK_OUT)
        self.click_random_enabled_day_in_calendar(HotelForm.HOTEL_CHECK_OUT)
        self.sleep(2)

    def check_dropdown_quantity(self):
        self.page_loaded(HotelForm.HOTEL_ROOM_FOR)
        self.is_element_present(HotelForm.HOTEL_ROOM_FOR)
        self.sleep(2)

    def click_to_list(self):
        self.page_loaded(HotelForm.HOTEL_ROOM_FOR)
        self.click_element(HotelForm.HOTEL_ROOM_FOR)
        self.sleep(2)

    def select_randomly_quantity(self):
        self.is_element_present(HotelForm.HOTEL_DROPDOWN_PLUS)
        self.do_randint_click(HotelForm.HOTEL_DROPDOWN_PLUS)
        self.is_element_present(HotelForm.HOTEL_DROPDOWN_MINUS)
        self.sleep(2)

    def assert_kids_quantity(self):
        self.is_element_present(HotelForm.HOTEL_QUANTITY_TEXT)
        self.is_visible(HotelForm.HOTEL_KIDS_COLUM)
        self.sleep(2)

    def assert_clickable_kids(self):
        self.assert_element_to_be_clickable(HotelForm.HOTEL_QUANTITY_KIDS)
        self.sleep(2)

    def check_the_search_button(self):
        self.is_element_present(HotelForm.HOTEL_SEARCH_BUTTON)
