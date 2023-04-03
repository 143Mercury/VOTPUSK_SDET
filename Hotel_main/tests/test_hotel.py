import time

from VOTPUSK.Hotel_main.Header.header_locator import HeaderHotelLocator
from VOTPUSK.Hotel_main.config.configuration import TestData
from VOTPUSK.Hotel_main.hotel_functionality.form.hotel_func_form import HotelForm
from VOTPUSK.Hotel_main.hotel_functionality.sliders_and_links_functionality.hotel_sliders_func_links import \
    SlidersHotelLinksLocator
from VOTPUSK.test.TestBase import BaseTest


class TestHotel(BaseTest):

    def test_header(self, driver):
        driver.get(TestData.URL)
        check_the_header = HeaderHotelLocator(driver)
        check_the_header.check_the_header()
        check_the_text_visibility = HeaderHotelLocator(driver)
        check_the_text_visibility.check_the_text_visibility()
        check_the_hotel_banner = HeaderHotelLocator(driver)
        check_the_hotel_banner.check_the_hotel_banner()

    def test_hotel_form_func(self, driver):
        driver.get(TestData.URL)
        check_the_total_hotel_form = HotelForm(driver)
        check_the_total_hotel_form.check_the_total_hotel_form()
        check_hotel_form_input_and_text = HotelForm(driver)
        check_hotel_form_input_and_text.check_hotel_form_input_and_text()
        hotel_input_city_and_click = HotelForm(driver)
        hotel_input_city_and_click.hotel_input_city_and_click()
        select_randomly_check_in_date = HotelForm(driver)
        select_randomly_check_in_date.select_randomly_check_in_date()
        check_dropdown_quantity = HotelForm(driver)
        check_dropdown_quantity.check_dropdown_quantity()
        select_randomly_quantity = HotelForm(driver)
        select_randomly_quantity.select_randomly_quantity()
        select_randomly_kids_quantity = HotelForm(driver)
        select_randomly_kids_quantity.select_randomly_kids_quantity()
        check_the_search_button = HotelForm(driver)
        check_the_search_button.check_the_search_button()

    def test_popular_design(self, driver):
        driver.get(TestData.URL)
        scroll_to_popular_sections = SlidersHotelLinksLocator(driver)
        scroll_to_popular_sections.scroll_to_popular_sections()
        check_the_text_h3 = SlidersHotelLinksLocator(driver)
        check_the_text_h3.check_the_text_h3()
        check_all_container_blocks = SlidersHotelLinksLocator(driver)
        check_all_container_blocks.check_all_container_blocks()
        check_all_same_hotel_locators = SlidersHotelLinksLocator(driver)
        check_all_same_hotel_locators.check_all_same_hotel_locators()
        check_link_under_line = SlidersHotelLinksLocator(driver)
        check_link_under_line.check_link_under_line()

    def test_hotels_offer(self, driver):
        driver.get(TestData.URL)
        scroll_into_view_hotels_offer = SlidersHotelLinksLocator(driver)
        scroll_into_view_hotels_offer.scroll_into_view_hotels_offer()
        time.sleep(3)
        check_the_h2 = SlidersHotelLinksLocator(driver)
        check_the_h2.check_the_h2()
        check_the_hotels_leaders_offer = SlidersHotelLinksLocator(driver)
        check_the_hotels_leaders_offer.check_the_hotels_leaders_offer()

    def test_hotel_comment_sections(self, driver):
        driver.get(TestData.URL)
        hotel_scroll_into_comment_section = SlidersHotelLinksLocator(driver)
        hotel_scroll_into_comment_section.hotel_scroll_into_comment_section()
        check_the_comment_blocks = SlidersHotelLinksLocator(driver)
        check_the_comment_blocks.check_the_comment_blocks()
        """check_comment_data = SlidersHotelLinksLocator(driver)
        check_comment_data.check_comment_data()"""
        assert_navigation_arrows_clickable = SlidersHotelLinksLocator(driver)
        assert_navigation_arrows_clickable.assert_navigation_arrows_clickable()
