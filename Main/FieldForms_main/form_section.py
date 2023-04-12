import time

from selenium.webdriver.common.by import By
from VOTPUSK.BaseMethods.object_methods import BaseMethods
from VOTPUSK.Main.Config.TestData import TestData
from VOTPUSK.Main.FieldForms_main.specifide_locators import SpecifiedLocators
from VOTPUSK.Main.FieldForms_main.world_type_locators import WorldTypeLocators
from VOTPUSK.Main.Config.TestDataWorld import TestDataWorld
from VOTPUSK.Main.FieldForms_main.hotel_locators import HotelFormLocators
from VOTPUSK.Main.Config.TestDataHotels import TestDataHotels
from selenium.webdriver.support.ui import WebDriverWait
from VOTPUSK.Main.FieldForms_main.train_locators import TrainLocators
from VOTPUSK.Main.Config.TestDataTrain import TestDataTrain
from VOTPUSK.Main.Config.TestDataRouts import TestDataRouts
from VOTPUSK.Main.FieldForms_main.routs_locators import RoutsLocators
from VOTPUSK.Main.FieldForms_main.country_and_cities import CountryAndCities


class ToursFormLocators(BaseMethods):
    PINNED_FORM = (By.CSS_SELECTOR, '[class="search"]')
    RTOURS_BUTTON = (By.CSS_SELECTOR, '[class="block-btns__btn block-btns__btn_active"]')
    WTOURS_BUTTON = (By.CSS_SELECTOR, '[class="block-btns__btn world-tours"]')
    SEARCH_BUTTON = (By.XPATH, '/html/body/section[2]/div/div[1]/form[2]/input')
    INPUT_CITY = (By.CSS_SELECTOR, '[id="s-query"]')
    CHOOSE_ATTR = (By.CSS_SELECTOR, '[class="search__item second typelist"]')
    SELECT_DATE_FROM = (By.CSS_SELECTOR, '[id="s-datefrom"]')
    SELECT_DATE_TO = (By.CSS_SELECTOR, '[id="s-dateto"]')
    MAIN_LOCATORS = [
        (By.XPATH, '/html/body/div[2]/div/div[2]'),
        (By.XPATH, '/html/body/div[2]/div/div[3]'),
        (By.XPATH, '/html/body/div[2]/div/div[4]'),
        (By.XPATH, '/html/body/div[2]/div/div[5]'),
        (By.CSS_SELECTOR, '[class="block-btns__btn block-btns__btn_active"]'),
        (By.CSS_SELECTOR, '[class="block-btns__btn world-tours"]'),

    ]
    LIST_DESTINATION = (By.CSS_SELECTOR, '[id="search-results-rutours"]')
    widget_date = (By.CSS_SELECTOR, '[id="ui-datepicker-div"]')
    CALENDAR_LOCATOR = (By.CSS_SELECTOR, '[class="ui-datepicker-calendar"]')
    CALENDAR_LOCATOR_NEXT = (By.CSS_SELECTOR, '[class="ui-datepicker ui-widget ui-widget-content ui-helper-clearfix '
                                              'ui-corner-all hotels-calendar tours-calendar"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
# Главная форма

    def type_section(self):
        for locators in self.MAIN_LOCATORS:
            section = self.assert_element_visibility(locators)
            return section

    def scroll_to_keys(self):
        self.window_scroll_by(0, 300)

    def form_keys(self):
        self.page_loaded(ToursFormLocators.INPUT_CITY)
        self.send_keys_to_element(ToursFormLocators.INPUT_CITY, TestData.CITY)

    def check_the_len_list(self):
        self.page_loaded(ToursFormLocators.LIST_DESTINATION)
        self.is_visible(ToursFormLocators.LIST_DESTINATION)
        self.sleep(3)

    def type_attraction(self):
        self.click_element(ToursFormLocators.CHOOSE_ATTR)
        self.page_loaded(ToursFormLocators.CHOOSE_ATTR)

    def check_the_attractions_container(self):
        self.is_element_present(SpecifiedLocators.ATTRACTIONS_CONTAINER)

    def do_random_click(self):
        self.click_random_locator(SpecifiedLocators.ATTRACTION)
        self.sleep(3)

    def do_double_click_calendar(self):
        self.is_element_present(ToursFormLocators.SELECT_DATE_FROM)
        self.double_click_element(ToursFormLocators.SELECT_DATE_FROM)
        self.sleep(2)

    def do_random_choice_date(self):
        self.is_element_present(ToursFormLocators.CALENDAR_LOCATOR)
        self.click_random_enabled_day_in_calendar(ToursFormLocators.CALENDAR_LOCATOR)
        self.sleep(2)

    def do_random_choice_next(self):
        self.is_element_present(ToursFormLocators.SELECT_DATE_TO)
        self.click_element(ToursFormLocators.SELECT_DATE_TO)
        self.click_random_enabled_day_in_calendar(ToursFormLocators.CALENDAR_LOCATOR_NEXT)
        self.sleep(2)

    def is_exist(self):
        self.is_element_present(ToursFormLocators.SEARCH_BUTTON)
        self.assert_element_to_be_clickable(ToursFormLocators.SEARCH_BUTTON)
        self.sleep(2)
# Форма поиска туров (World)

    def world_tour_switcher(self):
        self.is_element_present(WorldTypeLocators.WORLD_TOUR_SWITCHER)
        self.click_element(WorldTypeLocators.WORLD_TOUR_SWITCHER)
        self.sleep(2)

    def world_tour_input_form(self):
        self.is_element_present(WorldTypeLocators.WORLD_CITY_INPUT)
        self.page_loaded(WorldTypeLocators.WORLD_CITY_INPUT)
        self.send_keys_to_element(WorldTypeLocators.WORLD_CITY_INPUT, TestDataWorld.CITY_INPUT)
        self.sleep(2)

    def check_words_tour_len_list(self):
        self.page_loaded(WorldTypeLocators.WORLD_LEN_LIST)
        self.is_visible(WorldTypeLocators.WORLD_LEN_LIST)
        self.sleep(2)

    def witch_to_next_input_form(self):
        self.page_loaded(WorldTypeLocators.WORLD_CITY_INPUT)
        self.click_element(WorldTypeLocators.WORLD_CITY_INPUT)
        self.sleep(2)

    def send_keys_to_next_input_form(self):
        self.page_loaded(WorldTypeLocators.CITY_DEPARTURE_FIELD)
        self.send_keys_to_element(WorldTypeLocators.CITY_DEPARTURE_FIELD, TestDataWorld.DEPARTURE_INPUT)
        self.sleep(1)

    def scroll_to_world_tour(self):
        self.window_scroll_by(0, 125)
        self.sleep(1)

    def assert_calendar_enabled(self):
        self.is_element_present(WorldTypeLocators.CALENDAR_LOCATOR_WORLD)
        self.click_element(WorldTypeLocators.CALENDAR_LOCATOR_WORLD)
        self.sleep(2)

    def random_randint_choice(self):
        self.is_visible(WorldTypeLocators.CALENDAR_LOCATOR_WORLD_WIDGET)
        self.click_random_enabled_day_in_calendar(WorldTypeLocators.CALENDAR_LOCATOR_WORLD_WIDGET)
        self.sleep(3)

    def click_and_assert_modal_enabled(self):
        self.is_element_present(WorldTypeLocators.DURATION_DROPDOWN)
        self.click_element(WorldTypeLocators.DURATION_DROPDOWN)
        self.sleep(2)

    def random_randint_input_signs(self):
        self.is_element_present(WorldTypeLocators.INPUT_FROM)
        self.do_randint_click(WorldTypeLocators.INPUT_FROM)
        self.sleep(2)
        self.is_element_present(WorldTypeLocators.INPUT_TO)
        self.do_randint_click(WorldTypeLocators.INPUT_TO)
        self.sleep(2)

    # БАГ
    def check_visibility_tourist_quantity_modal(self):
        self.is_element_present(WorldTypeLocators.TOURIST_QUANTITY)
        self.assert_element_to_be_clickable(WorldTypeLocators.TOURIST_QUANTITY)
        self.sleep(2)

    def click_to_quantity_modal(self):
        self.click_element(WorldTypeLocators.TOURIST_QUANTITY)
        self.do_randint_click(WorldTypeLocators.TOURIST_QUANTITY_SCROLLER)
        self.sleep(2)

    def assert_kids_quantity(self):
        self.is_element_present(WorldTypeLocators.TOURIST_QUANTITY_KIDS)
        self.click_element(WorldTypeLocators.TOURIST_QUANTITY_KIDS)
        self.sleep(2)

    def random_randint_click_kids_choice(self):
        self.page_loaded(WorldTypeLocators.TOURIST_QUANTITY_KIDS_RANDOM_CHOICE)
        self.click_element(WorldTypeLocators.TOURIST_QUANTITY_KIDS_RANDOM_CHOICE)
        self.sleep(2)

    def check_the_visibility_search_button(self):
        self.is_element_present(WorldTypeLocators.CHECK_BUTTON)
        self.assert_element_to_be_clickable(WorldTypeLocators.CHECK_BUTTON)
        self.sleep(2)

    def check_the_blocks_add_buttons(self):
        self.is_visible(WorldTypeLocators.TOURS_BLOCKS_TRAVEL_BUTTONS)
# Форма поиска отелей

    def switch_to_hotels(self):
        self.page_loaded(HotelFormLocators.OPTION_SWITCHER_HOTEL)
        self.click_element(HotelFormLocators.OPTION_SWITCHER_HOTEL)
        self.sleep(2)

    def scroll_page_into_view(self):
        self.window_scroll_by(0, 125)

    def do_send_keys_hotel(self):
        self.is_element_present(HotelFormLocators.HOTEL_KEYS_INPUT)
        self.send_keys_to_element(HotelFormLocators.HOTEL_KEYS_INPUT, TestDataHotels.INPUT_CITY_COUNTRY_HOTEL)
        self.sleep(2)

    def do_click_on_check_in_option(self):
        self.is_element_present(HotelFormLocators.HOTEL_CHECK_IN)
        self.click_element(HotelFormLocators.HOTEL_CHECK_IN)
        self.sleep(2)

    def wait_until_widget_loaded(self):
        self.page_loaded(HotelFormLocators.HOTEL_CHECK_IN_WIDGET)
        self.sleep(2)

    def randint_click_to_check_in(self):
        self.click_random_enabled_day_in_calendar(HotelFormLocators.HOTEL_CHECK_IN_WIDGET)
        self.sleep(2)

    """def do_wait_until_element_load_and_randomly_choose_check_out(self):
        self.wait_for_element(HotelFormLocators.HOTEL_CHECK_OUT_WIDGET)
        self.assert_element_visibility(HotelFormLocators.HOTEL_CHECK_OUT_WIDGET)
        self.click_random_enabled_day_in_calendar(HotelFormLocators.HOTEL_CHECK_OUT_WIDGET)"""

    def open_dropdown_quantity(self):
        self.is_element_present(HotelFormLocators.DROPDOWN_ADD_ADULTS)
        self.click_element(HotelFormLocators.DROPDOWN_ADD_ADULTS)
        self.sleep(2)

    def random_randint_click_adults_opt(self):
        self.is_element_present(HotelFormLocators.ADD_ADULTS_OPTION)
        self.do_randint_click(HotelFormLocators.ADD_ADULTS_OPTION)
        self.sleep(2)

    def open_dropdown_kids(self):
        self.is_element_present(HotelFormLocators.DROPDOWN_OPEN_KIDS)
        self.click_element(HotelFormLocators.DROPDOWN_OPEN_KIDS)
        self.sleep(2)

    def select_widget_item(self):
        self.is_element_present(HotelFormLocators.DROPDOWN_GET_ALL_WIDGET)
        self.click_element(HotelFormLocators.DROPDOWN_GET_ALL_WIDGET)
        self.sleep(2)

    def check_visibility_search_button(self):
        self.is_element_present(HotelFormLocators.HOTEL_SEARCH_BUTTON)
        self.assert_element_to_be_clickable(HotelFormLocators.HOTEL_SEARCH_BUTTON)
        self.sleep(2)

    # Форма поиска Жд билеты
    def switch_to_train_option(self):
        self.page_loaded(TrainLocators.TRAIN_SWITCHER)
        self.click_element(TrainLocators.TRAIN_SWITCHER)
        self.sleep(2)

    def do_send_keys_to_input_form_from(self):
        self.page_loaded(TrainLocators.CITY_INPUT_FROM)
        self.send_keys_to_element(TrainLocators.CITY_INPUT_FROM, TestDataTrain.CITY_INPUT_THERE)
        self.sleep(2)

    def do_send_keys_to_input_form_to(self):
        self.is_element_present(TrainLocators.CITY_INPUT_FROM)
        self.send_keys_to_element(TrainLocators.CITY_INPUT_TO, TestDataTrain.CITY_INPUT_BACK)
        self.sleep(2)

    def do_click_to_calendar_option(self):
        self.is_element_present(TrainLocators.TRAIN_CALENDAR_TO)
        self.click_element(TrainLocators.TRAIN_CALENDAR_TO)
        self.sleep(2)

    def scroll_page_into_element_view(self):
        self.window_scroll_by(0, 125)
        self.sleep(2)

    def do_random_choice_calendar_date(self):
        self.page_loaded(TrainLocators.TRAIN_CALENDAR_TO_WIDGET)
        self.click_random_enabled_day_in_calendar(TrainLocators.TRAIN_CALENDAR_TO_WIDGET)
        self.sleep(2)

    def do_check_search_button_visibility(self):
        self.page_loaded(TrainLocators.TRAIN_SEARCH_BUTTON)
        self.assert_element_to_be_clickable(TrainLocators.TRAIN_SEARCH_BUTTON)

# Форма маршруты

    def do_switch_to_routs(self):
        self.page_loaded(RoutsLocators.ROUTS_SWITCHER)
        self.click_element(RoutsLocators.ROUTS_SWITCHER)
        self.sleep(2)

    def do_send_keys_routs_first(self):
        self.is_element_present(RoutsLocators.FROM_WHERE)
        self.send_keys_to_element(RoutsLocators.FROM_WHERE, TestDataRouts.ROUTS_KEYS_TO)
        self.sleep(2)

    def assert_routs_from_len_list(self):
        self.is_visible(RoutsLocators.ROUTS_LEN_LIST)
        self.sleep(2)

    def do_send_keys_routs_second(self):
        self.page_loaded(RoutsLocators.TO_THERE)
        self.send_keys_to_element(RoutsLocators.TO_THERE, TestDataRouts.ROUTS_KEYS_FROM)
        self.sleep(2)

    def assert_routs_to_len_list(self):
        self.is_visible(RoutsLocators.ROUTS_LEN_LIST)
        self.sleep(2)

    def do_check_search_routs_button(self):
        self.page_loaded(RoutsLocators.SEARCH_ROUTS_BUTTON)
        self.is_element_present(RoutsLocators.SEARCH_ROUTS_BUTTON)

# Форма Страны и города
    def switch_to_country_and_cities_option(self):
        self.is_element_present(CountryAndCities.COUNTRY_SWITCHER)
        self.click_element(CountryAndCities.COUNTRY_SWITCHER)
        self.sleep(2)

    def check_the_total_form(self):
        self.is_element_present(CountryAndCities.SELECT_COUNTRY)
        self.click_element(CountryAndCities.SELECT_COUNTRY)
        self.sleep(2)

    def random_select_country(self):
        self.random_country_selection(CountryAndCities.CITIES_AND_COUNTRY_CONTAINER)
        self.is_element_present(CountryAndCities.SELECT_CITIES)
        self.sleep(2)

    def random_select_city(self):
        self.page_loaded(CountryAndCities.SELECT_CITIES)
        self.click_element(CountryAndCities.SELECT_CITIES)
        self.random_country_selection(CountryAndCities.CITIES_AND_COUNTRY_CONTAINER)
        self.sleep(2)

    def random_select_cities_and_check_the_search_button(self):
        self.is_element_present(CountryAndCities.SEARCH_COUNTRY_AND_CITIES_BUTTON)