from selenium.webdriver.common.by import By
from VOTPUSK.BaseMethods.object_methods import BaseMethods
from VOTPUSK.Hotel_main.hotels_second_page.config.configuration import TestDataSecondPage


class FiltersLocators(BaseMethods):
    PRICE_RANGE_CONTAINER = (By.XPATH, '//*[@id="filter-hotels"]/div[1]')
    PRICE_P = (By.XPATH, '//*[@id="filter-hotels"]/div[1]/div[1]/p')
    PRICE_SLIDER = (By.CSS_SELECTOR, '[class="slider-range price-range ui-slider ui-corner-all ui-slider-horizontal '
                                     'ui-widget ui-widget-content"]')
    PRICE_RANGE_HIDDEN = (By.XPATH, '//*[@id="filter-hotels"]/div[1]/div[1]/svg')
    FILTER_COST_BLOCK = (By.ID, 'filter-cost')
    FILTER_COST_FROM = (By.XPATH, '//*[@id="filter-cost"]/div[1]/input')
    FILTER_COST_TO = (By.XPATH, '//*[@id="filter-cost"]/div[2]/input')

    HOTEL_STAR_RATING_CONTAINER = (By.XPATH, '//*[@id="filter-hotels"]/div[2]')
    HOTEL_RATING_P = (By.XPATH, '//*[@id="filter-hotels"]/div[2]/div[1]/p')
    CHECK_BOX_NULL = (By.CSS_SELECTOR, '[for="hotel-stars-0"]')
    CHECK_BOX_1_STAR = (By.CSS_SELECTOR, '[for="hotel-stars-1"]')
    CHECK_BOX_2_STAR = (By.CSS_SELECTOR, '[for="hotel-stars-2"]')
    CHECK_BOX_3_STAR = (By.CSS_SELECTOR, '[for="hotel-stars-3"]')
    CHECK_BOX_4_STAR = (By.CSS_SELECTOR, '[for="hotel-stars-4"]')
    CHECK_BOX_5_STAR = (By.CSS_SELECTOR, '[for="hotel-stars-5"]')
    STAR_RATING_HIDDEN_ARROW = (By.XPATH, '//*[@id="filter-hotels"]/div[2]/div[1]/svg')

    HOTEL_RATING = (By.XPATH, '//*[@id="filter-hotels"]/div[3]')
    RATING_CONTAINER = (By.CSS_SELECTOR, '[class="add-active add-active--orange hotels-rating"]')
    ANY_RATING = (By.CSS_SELECTOR, '[class="add-active__item active hotels-rating__any"]')
    RATING_6 = (By.XPATH, '//*[@id="filter-hotels"]/div[3]/div[2]/div/div/div[2]')
    RATING_7 = (By.XPATH, '//*[@id="filter-hotels"]/div[3]/div[2]/div/div/div[3]')
    RATING_8 = (By.XPATH, '//*[@id="filter-hotels"]/div[3]/div[2]/div/div/div[4]')
    RATING_9 = (By.XPATH, '//*[@id="filter-hotels"]/div[3]/div[2]/div/div/div[5]')
    RATING_HIDDEN_ARROW = (By.XPATH, '//*[@id="filter-hotels"]/div[3]/div[1]/svg')

    BLOCK_SLIDER_DISTANCE_TH_THE_CENTER = (By.XPATH, '//*[@id="filter-hotels"]/div[4]')
    DISTANCE_TO_THE_CENTER_P = (By.XPATH, '//*[@id="filter-hotels"]/div[4]/div[1]/p')
    DISTANCE_TO_THE_CENTER_H6 = (By.ID, 'filter-distance')
    DISTANCE_TO_THE_CENTER_HIDDEN_ARROW = (By.XPATH, '//*[@id="filter-hotels"]/div[4]/div[1]/svg')
    DISTANCE_TO_THE_CENTER_SLIDER = (By.CSS_SELECTOR, '[class="ui-slider-range ui-corner-all ui-widget-header '
                                                      'ui-slider-range-min"]')

    TYPE_OF_APARTMENTS_CONTAINER = (By.XPATH, '//*[@id="filter-hotels"]/div[5]')
    TYPE_OF_APARTMENTS_P = (By.XPATH, '//*[@id="filter-hotels"]/div[5]/div[1]/p')
    CHECK_BOX_1 = (By.CSS_SELECTOR, '[for="hotel_types_1"]')
    CHECK_BOX_2 = (By.CSS_SELECTOR, '[for="hotel_types_4"]')
    CHECK_BOX_3 = (By.CSS_SELECTOR, '[for="hotel_types_6"]')
    CHECK_BOX_4 = (By.CSS_SELECTOR, '[for="hotel_types_8"]')
    TYPE_OF_APARTMENTS_HIDDEN_ARROW = (By.XPATH, '//*[@id="filter-hotels"]/div[5]/div[1]/svg')
    TYPE_OF_APARTMENTS_HIDDEN_LINK = (By.XPATH, '//*[@id="filter_data_hotel_types"]/div[7]/div[2]')

    AMENITIES_IN_THE_HOTEL = (By.XPATH, '//*[@id="filter-hotels"]/div[6]')
    AMENITIES_IN_THE_HOTEL_P = (By.XPATH, '//*[@id="filter-hotels"]/div[6]/div[1]/p')
    AMENITIES_CHECK_BOX_1 = (By.CSS_SELECTOR, '[for="amenities_1"]')
    AMENITIES_CHECK_BOX_2 = (By.CSS_SELECTOR, '[for="amenities_2"]')
    AMENITIES_CHECK_BOX_3 = (By.CSS_SELECTOR, '[for="amenities_3"]')
    AMENITIES_CHECK_BOX_4 = (By.CSS_SELECTOR, '[for="amenities_8"]')

    AMENITIES_HIDDEN_LINK = (By.XPATH, '//*[@id="filter_data_amenities"]/div[7]/div[2]')
    AMENITIES_HIDDEN_UPPER_LINK = (By.XPATH, '//*[@id="filter-hotels"]/div[6]/div[1]/svg')

    AMENITIES_IN_THE_ROOM_CONTAINER = (By.XPATH, '//*[@id="filter-hotels"]/div[7]')
    AMENITIES_IN_THE_ROOM_CHECK_BOX_1 = (By.CSS_SELECTOR, '[for="short_amenities_1"]')
    AMENITIES_IN_THE_ROOM_CHECK_BOX_2 = (By.CSS_SELECTOR, '[for="short_amenities_2"]')
    AMENITIES_IN_THE_ROOM_CHECK_BOX_3 = (By.CSS_SELECTOR, '[for="short_amenities_4"]')
    AMENITIES_IN_THE_ROOM_CHECK_BOX_4 = (By.CSS_SELECTOR, '[for="short_amenities_8"]')

    AMENITIES_IN_THE_ROOM_HIDDEN_LINK = (By.XPATH, '//*[@id="filter_data_short_amenities"]/div[7]/div[2]')
    AMENITIES_IN_THE_ROOM_HIDDEN_UPPER_LINK = (By.XPATH, '//*[@id="filter-hotels"]/div[7]/div[1]/svg')

    CLEAR_DEFAULT_OPTIONS = (By.XPATH, '//*[@id="filter-hotels"]/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_visibility_range_block(self):
        self.is_element_present(FiltersLocators.PRICE_RANGE_CONTAINER)

    def assert_short_details_on_block(self):
        self.is_visible(FiltersLocators.PRICE_P)

    def scroll_to_average_price_slider(self):
        self.move_slider(FiltersLocators.PRICE_SLIDER, 0, 100)

    def check_hidden_arrow(self):
        self.is_element_present(FiltersLocators.PRICE_RANGE_HIDDEN)
        self.assert_element_to_be_clickable(FiltersLocators.PRICE_RANGE_HIDDEN)

    def assert_cost_block(self):
        self.is_element_present(FiltersLocators.FILTER_COST_BLOCK)

    def clear_and_check_functionality_field_form_from(self):
        self.is_element_present(FiltersLocators.FILTER_COST_FROM)
        self.sleep(1)
        self.send_keys_to_element(FiltersLocators.FILTER_COST_FROM, TestDataSecondPage.PRICE_RANGE_FROM)

    def clear_and_check_functionality_field_form_to(self):
        self.is_element_present(FiltersLocators.FILTER_COST_TO)
        self.sleep(1)
        self.send_keys_to_element(FiltersLocators.FILTER_COST_TO, TestDataSecondPage.PRICE_RANGE_TO)

    # Звёздность отеля
    def check_star_rating_container_hotel_present(self):
        self.is_element_present(FiltersLocators.HOTEL_STAR_RATING_CONTAINER)

    def check_data_name_p(self):
        self.is_visible(FiltersLocators.HOTEL_RATING_P)

    def check_the_check_box_rating(self):
        self.is_element_present(FiltersLocators.CHECK_BOX_NULL)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_NULL)
        self.sleep(2)
        self.is_element_present(FiltersLocators.CHECK_BOX_1_STAR)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_1_STAR)
        self.sleep(2)
        self.is_element_present(FiltersLocators.CHECK_BOX_2_STAR)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_2_STAR)
        self.sleep(2)
        self.is_element_present(FiltersLocators.CHECK_BOX_3_STAR)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_3_STAR)
        self.sleep(2)
        self.is_element_present(FiltersLocators.CHECK_BOX_4_STAR)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_4_STAR)
        self.sleep(2)
        self.is_element_present(FiltersLocators.CHECK_BOX_5_STAR)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_5_STAR)

    def check_the_visibility_and_clickable_hidden_arrow(self):
        self.is_element_present(FiltersLocators.STAR_RATING_HIDDEN_ARROW)
        self.assert_element_to_be_clickable(FiltersLocators.STAR_RATING_HIDDEN_ARROW)

    # Рейтинг отеля
    def check_hotel_rating_container(self):
        self.is_element_present(FiltersLocators.HOTEL_RATING)

    def check_rating_blocks(self):
        self.is_element_present(FiltersLocators.RATING_CONTAINER)
        self.assert_element_to_be_clickable(FiltersLocators.RATING_CONTAINER)
        self.sleep(1)

    def check_each_rating_blocks(self):
        self.is_element_present(FiltersLocators.ANY_RATING)
        self.assert_element_to_be_clickable(FiltersLocators.ANY_RATING)
        self.sleep(1)
        self.is_element_present(FiltersLocators.RATING_6)
        self.assert_element_to_be_clickable(FiltersLocators.RATING_6)
        self.sleep(1)
        self.is_element_present(FiltersLocators.RATING_7)
        self.assert_element_to_be_clickable(FiltersLocators.RATING_7)
        self.sleep(1)
        self.is_element_present(FiltersLocators.RATING_8)
        self.assert_element_to_be_clickable(FiltersLocators.RATING_8)
        self.sleep(1)
        self.is_element_present(FiltersLocators.RATING_9)
        self.assert_element_to_be_clickable(FiltersLocators.RATING_9)

    def check_visibility_hidden_arrow(self):
        self.is_element_present(FiltersLocators.RATING_HIDDEN_ARROW)
        self.sleep(1)
        self.assert_element_to_be_clickable(FiltersLocators.RATING_HIDDEN_ARROW)

    # Расстояние до центра
    def scroll_range_slider(self):
        self.move_slider(FiltersLocators.BLOCK_SLIDER_DISTANCE_TH_THE_CENTER, 0, 100)

    def check_the_h3(self):
        self.is_visible(FiltersLocators.DISTANCE_TO_THE_CENTER_P)
        self.sleep(1)
        self.is_visible(FiltersLocators.DISTANCE_TO_THE_CENTER_H6)

    def check_hidden_upper_arrow(self):
        self.is_element_present(FiltersLocators.DISTANCE_TO_THE_CENTER_HIDDEN_ARROW)
        self.sleep(1)
        self.assert_element_to_be_clickable(FiltersLocators.DISTANCE_TO_THE_CENTER_HIDDEN_ARROW)

    # Тип жилья
    def check_type_of_apartments_container(self):
        self.is_element_present(FiltersLocators.TYPE_OF_APARTMENTS_CONTAINER)

    def check_the_h6_data_name(self):
        self.is_visible(FiltersLocators.TYPE_OF_APARTMENTS_P)

    def assert_check_boxes(self):
        self.is_element_present(FiltersLocators.CHECK_BOX_1)
        self.sleep(1)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_1)
        self.is_element_present(FiltersLocators.CHECK_BOX_2)
        self.sleep(1)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_2)
        self.is_element_present(FiltersLocators.CHECK_BOX_3)
        self.sleep(1)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_3)
        self.is_element_present(FiltersLocators.CHECK_BOX_4)
        self.sleep(1)
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_4)

    def check_hidden_arrow_type_of_apartments(self):
        self.is_element_present(FiltersLocators.TYPE_OF_APARTMENTS_HIDDEN_ARROW)
        self.assert_element_to_be_clickable(FiltersLocators.TYPE_OF_APARTMENTS_HIDDEN_ARROW)

    def check_the_under_hidden_link(self):
        self.is_element_present(FiltersLocators.TYPE_OF_APARTMENTS_HIDDEN_LINK)
        self.assert_element_to_be_clickable(FiltersLocators.TYPE_OF_APARTMENTS_HIDDEN_LINK)
