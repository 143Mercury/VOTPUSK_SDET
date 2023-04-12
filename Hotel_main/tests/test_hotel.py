import time
import pytest

from VOTPUSK.Hotel_main.Header.header_locator import HeaderHotelLocator
from VOTPUSK.Hotel_main.config.configuration import TestData
from VOTPUSK.Hotel_main.hotel_functionality.form.hotel_func_form import HotelForm
from VOTPUSK.Hotel_main.hotel_functionality.sliders_and_links_functionality.hotel_sliders_func_links\
    import\
    SlidersHotelLinksLocator
from VOTPUSK.Main.test.TestBase import BaseTest


class TestHotel(BaseTest):

    @pytest.mark.smoke
    def test_header(self, driver):
        driver.get(TestData.URL)
        check_the_header = HeaderHotelLocator(driver)
        check_the_header.check_the_header()
        check_the_text_visibility = HeaderHotelLocator(driver)
        check_the_text_visibility.check_the_text_visibility()
        check_the_hotel_banner = HeaderHotelLocator(driver)
        check_the_hotel_banner.check_the_hotel_banner()

    @pytest.mark.smoke
    def test_hotel_form_func(self, driver):
        driver.get(TestData.URL)
        check_the_main_hotel_form = HotelForm(driver)
        check_the_main_hotel_form.check_the_main_hotel_form()
        wait_until_page_load_and_assert_elements = HotelForm(driver)
        wait_until_page_load_and_assert_elements.wait_until_page_load_and_assert_elements()
        send_keys_to_hotel_form = HotelForm(driver)
        send_keys_to_hotel_form.send_keys_to_hotel_form()
        assert_hotel_dropdown_present = HotelForm(driver)
        assert_hotel_dropdown_present.assert_hotel_dropdown_present()
        select_randomly_check_in_date = HotelForm(driver)
        select_randomly_check_in_date.select_randomly_check_in_date()
        select_randomly_check_out_date = HotelForm(driver)
        select_randomly_check_out_date.select_randomly_check_out_date()
        check_dropdown_quantity = HotelForm(driver)
        check_dropdown_quantity.check_dropdown_quantity()
        click_to_list = HotelForm(driver)
        click_to_list.click_to_list()
        select_randomly_quantity = HotelForm(driver)
        select_randomly_quantity.select_randomly_quantity()
        assert_kids_quantity = HotelForm(driver)
        assert_kids_quantity.assert_kids_quantity()
        assert_clickable_kids = HotelForm(driver)
        assert_clickable_kids.assert_clickable_kids()
        check_the_search_button = HotelForm(driver)
        check_the_search_button.check_the_search_button()

    @pytest.mark.smoke
    def test_popular_design(self, driver):
        driver.get(TestData.URL)
        scroll_to_popular_sections = SlidersHotelLinksLocator(driver)
        scroll_to_popular_sections.scroll_to_popular_sections()
        check_the_text_h3 = SlidersHotelLinksLocator(driver)
        check_the_text_h3.check_the_text_h3()
        check_all_same_hotel_locators_1_4 = SlidersHotelLinksLocator(driver)
        check_all_same_hotel_locators_1_4.check_all_same_hotel_locators_1_4()
        check_all_same_hotel_locators_5_8 = SlidersHotelLinksLocator(driver)
        check_all_same_hotel_locators_5_8.check_all_same_hotel_locators_5_8()
        check_link_under_line = SlidersHotelLinksLocator(driver)
        check_link_under_line.check_link_under_line()

    @pytest.mark.smoke
    def test_hotels_offer(self, driver):
        driver.get(TestData.URL)
        scroll_into_view_hotels_offer = SlidersHotelLinksLocator(driver)
        scroll_into_view_hotels_offer.scroll_into_view_hotels_offer()
        check_the_h2 = SlidersHotelLinksLocator(driver)
        check_the_h2.check_the_h2()
        check_the_hotels_leaders_offer_1_2 = SlidersHotelLinksLocator(driver)
        check_the_hotels_leaders_offer_1_2.check_the_hotels_leaders_offer_1_2()
        check_the_hotels_leaders_offer_5_8 = SlidersHotelLinksLocator(driver)
        check_the_hotels_leaders_offer_5_8.check_the_hotels_leaders_offer_5_8()

    @pytest.mark.smoke
    def test_hotel_comment_sections(self, driver):
        driver.get(TestData.URL)
        hotel_scroll_into_comment_section = SlidersHotelLinksLocator(driver)
        hotel_scroll_into_comment_section.hotel_scroll_into_comment_section()
        check_the_comment_blocks = SlidersHotelLinksLocator(driver)
        check_the_comment_blocks.check_the_comment_blocks()
        assert_navigation_arrow_next_clickable = SlidersHotelLinksLocator(driver)
        assert_navigation_arrow_next_clickable.assert_navigation_arrow_next_clickable()
        assert_navigation_arrow_prev_clickable = SlidersHotelLinksLocator(driver)
        assert_navigation_arrow_prev_clickable.assert_navigation_arrow_prev_clickable()

    @pytest.mark.smoke
    def test_faq_hotel(self, driver):
        driver.get(TestData.URL)
        scroll_to_FAQ = SlidersHotelLinksLocator(driver)
        scroll_to_FAQ.scroll_to_FAQ()
        check_response_container = SlidersHotelLinksLocator(driver)
        check_response_container.check_response_container()
        check_adjust_blocks_1 = SlidersHotelLinksLocator(driver)
        check_adjust_blocks_1.check_adjust_blocks_1()
        check_adjust_blocks_2 = SlidersHotelLinksLocator(driver)
        check_adjust_blocks_2.check_adjust_blocks_2()
        check_adjust_blocks_3 = SlidersHotelLinksLocator(driver)
        check_adjust_blocks_3.check_adjust_blocks_3()
        check_adjust_blocks_4 = SlidersHotelLinksLocator(driver)
        check_adjust_blocks_4.check_adjust_blocks_4()
        check_adjust_blocks_5 = SlidersHotelLinksLocator(driver)
        check_adjust_blocks_5.check_adjust_blocks_5()
        check_adjust_blocks_6 = SlidersHotelLinksLocator(driver)
        check_adjust_blocks_6.check_adjust_blocks_6()
        check_adjust_blocks_7 = SlidersHotelLinksLocator(driver)
        check_adjust_blocks_7.check_adjust_blocks_7()
        check_adjust_blocks_8 = SlidersHotelLinksLocator(driver)
        check_adjust_blocks_8.check_adjust_blocks_8()
        checking_clickable_faq = SlidersHotelLinksLocator(driver)
        checking_clickable_faq.checking_clickable_faq()
        check_hotel_faq_link_under_line = SlidersHotelLinksLocator(driver)
        check_hotel_faq_link_under_line.check_hotel_faq_link_under_line()

