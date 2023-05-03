import pytest
from VOTPUSK.Main.Header.header_info import HeaderLocators
from VOTPUSK.Main.Config.TestData import TestData
from VOTPUSK.Main.Title.title import TitleLocator
from VOTPUSK.Main.test.TestBase import BaseTest
from VOTPUSK.Main.FieldForms_main.form_section import ToursFormLocators
from VOTPUSK.Main.Sliders.sliders_section import SliderSection


class TestPage(BaseTest):
    def test_header(self, driver):
        driver.get(TestData.URL)
        header_info = HeaderLocators(driver)
        header_info.header_info()
        burger_menu = HeaderLocators(driver)
        burger_menu.burger_menu()
        logo_info = HeaderLocators(driver)
        logo_info.logo_info()

    @pytest.mark.smoke()
    def test_title(self, driver):
        driver.get(TestData.URL)
        title_visible = TitleLocator(driver)
        title_visible.title_is_exist()

    @pytest.mark.smoke()
    def test_field_form(self, driver):
        driver.get(TestData.URL)

    def test_form(self, driver):
        driver.get(TestData.URL)
        pinned_form = ToursFormLocators(driver)
        pinned_form.pinned_form()

    def test_typeSection(self, driver):
        driver.get(TestData.URL)
        section = ToursFormLocators(driver)
        section.type_section()

    def test_russian_tour(self, driver):
        driver.get(TestData.URL)
        city_field = ToursFormLocators(driver)
        city_field.form_keys()
        click_on_attraction = ToursFormLocators(driver)
        click_on_attraction.type_attraction()
        random_click_on_attraction = ToursFormLocators(driver)
        random_click_on_attraction.do_random_click()
        do_double_click_on_calendar = ToursFormLocators(driver)
        do_double_click_on_calendar.do_double_click_calendar()
        do_random_choice_on_calendar = ToursFormLocators(driver)
        do_random_choice_on_calendar.do_random_choice_date()
        do_random_choice_and_click_on_calendar_next = ToursFormLocators(driver)
        do_random_choice_and_click_on_calendar_next.do_random_choice_next()
        check_the_next_button = ToursFormLocators(driver)
        check_the_next_button.is_exist()

    def test_world_tour(self, driver):
        driver.get(TestData.URL)
        switch_option = ToursFormLocators(driver)
        switch_option.world_tour_switcher()
        input_field_city_and_clear_default_value = ToursFormLocators(driver)
        input_field_city_and_clear_default_value.world_tour_input_form()
        scroll_to_world_tour = ToursFormLocators(driver)
        scroll_to_world_tour.scroll_to_world_tour()
        do_random_choice_calendar = ToursFormLocators(driver)
        do_random_choice_calendar.do_random_choice_calendar()
        do_click_to_dropdown_duration = ToursFormLocators(driver)
        do_click_to_dropdown_duration.do_random_choice_duration_nights()
        do_random_choice_duration_nights = ToursFormLocators(driver)
        do_random_choice_duration_nights.do_random_choice_kids()
        do_click_quantity_tourist_dropdown_and_random_choice = ToursFormLocators(driver)
        do_click_quantity_tourist_dropdown_and_random_choice.do_random_choice_tourist_quantity()
        do_open_dropdown_kids = ToursFormLocators(driver)
        do_open_dropdown_kids.do_random_choice_kids()
        check_the_search_button = ToursFormLocators(driver)
        check_the_search_button.check_the_visibility_search_button()
        check_the_blocks_add_buttons = ToursFormLocators(driver)
        check_the_blocks_add_buttons.check_the_blocks_add_buttons()

    def test_hotel_options(self, driver):
        driver.get(TestData.URL)
        switch_options_to_hotel = ToursFormLocators(driver)
        switch_options_to_hotel.switch_to_hotels()
        do_send_keys_field_input_hotels = ToursFormLocators(driver)
        do_send_keys_field_input_hotels.do_send_keys_hotel()
        do_click_on_calendar = ToursFormLocators(driver)
        do_click_on_calendar.do_click_on_check_in_option()
        do_wait_until_element_load = ToursFormLocators(driver)
        do_wait_until_element_load.do_wait_until_element_load_and_randomly_choose_check_in()
        do_open_dropdown_quantity = ToursFormLocators(driver)
        do_open_dropdown_quantity.open_dropdown_quantity()
        do_open_dropdown_quantity_kids = ToursFormLocators(driver)
        do_open_dropdown_quantity_kids.open_dropdown_kids()
        do_check_visibility_search_button = ToursFormLocators(driver)
        do_check_visibility_search_button.check_the_visibility_search_button()

    def test_train_options(self, driver):
        driver.get(TestData.URL)
        switch_to_train = ToursFormLocators(driver)
        switch_to_train.switch_to_train_option()
        do_send_keys_to_form_from = ToursFormLocators(driver)
        do_send_keys_to_form_from.do_send_keys_to_input_form_from()
        do_send_keys_to_form_to = ToursFormLocators(driver)
        do_send_keys_to_form_to.do_send_keys_to_input_form_to()
        do_click_to_calendar_option = ToursFormLocators(driver)
        do_click_to_calendar_option.do_click_to_calendar_option()
        do_random_choice_to_calendar_date = ToursFormLocators(driver)
        do_random_choice_to_calendar_date.do_random_choice_calendar_date()
        do_check_search_button = ToursFormLocators(driver)
        do_check_search_button.do_check_search_button_visibility()

    def test_routs_option(self, driver):
        driver.get(TestData.URL)
        switch_to_routs = ToursFormLocators(driver)
        switch_to_routs.do_switch_to_routs()
        do_send_keys_to_routs_from = ToursFormLocators(driver)
        do_send_keys_to_routs_from.do_send_keys_routs_first()
        do_send_keys_to_routs_to = ToursFormLocators(driver)
        do_send_keys_to_routs_to.do_send_keys_routs_second()
        do_check_search_routs_button = ToursFormLocators(driver)
        do_check_search_routs_button.do_check_search_routs_button()

    def test_country_And_cities(self, driver):
        driver.get(TestData.URL)
        switch_option = ToursFormLocators(driver)
        switch_option.switch_to_country_and_cities_option()
        check_the_total_form_and_click = ToursFormLocators(driver)
        check_the_total_form_and_click.check_the_total_form()
        random_select_country = ToursFormLocators(driver)
        random_select_country.random_select_country()
        random_select_cities = ToursFormLocators(driver)
        random_select_cities.random_select_cities_and_check_the_search_button()

    def test_tours_wrapper(self, driver):
        driver.get(TestData.URL)
        check_wrapper = SliderSection(driver)
        check_wrapper.do_check_block_tours_option()

    def test_tours_slider(self, driver):
        driver.get(TestData.URL)
        scroll_page = SliderSection(driver)
        scroll_page.scroll_page_tours()
        check_container_scroll_slider_and_check_again = SliderSection(driver)
        check_container_scroll_slider_and_check_again.check_tour_container()
        check_the_first_block = SliderSection(driver)
        check_the_first_block.check_each_blocks_to_exist_tours_first()
        move_to_next_blocks = SliderSection(driver)
        move_to_next_blocks.check_each_blocks_to_exist()
        check_container_again = SliderSection(driver)
        check_container_again.check_tour_container_again()
        switch_tour_section = SliderSection(driver)
        switch_tour_section.switch_tour_section()
        check_the_container_inside = SliderSection(driver)
        check_the_container_inside.check_the_container_inside()
        slide_to_next_blocks = SliderSection(driver)
        slide_to_next_blocks.slide_to_next_blocks()
        check_the_tour_order_button = SliderSection(driver)
        check_the_tour_order_button.check_the_tour_order_button()

    def test_articles_container(self, driver):
        driver.get(TestData.URL)
        scroll_to_page_articles = SliderSection(driver)
        scroll_to_page_articles.scroll_to_page_articles()
        check_the_block_of_articles = SliderSection(driver)
        check_the_block_of_articles.check_the_block_of_articles()
        scroll_and_check_the_blocks_container = SliderSection(driver)
        scroll_and_check_the_blocks_container.scroll_and_check_the_blocks_container()
        scroll_and_check_the_blocks_container = SliderSection(driver)
        scroll_and_check_the_blocks_container.scroll_and_check_the_blocks_container()
        check_all_item_container = SliderSection(driver)
        check_all_item_container.check_all_item_container()
        check_all_article_item = SliderSection(driver)
        check_all_article_item.check_all_article_item()
        check_form_block = SliderSection(driver)
        check_form_block.check_form_block()
        do_random_select_country_city_themes = SliderSection(driver)
        do_random_select_country_city_themes.do_random_select_country_city_themes()
        check_articles_search_hutton = SliderSection(driver)
        check_articles_search_hutton.check_articles_search_hutton()

    def test_attractions_container(self, driver):
        driver.get(TestData.URL)
        scroll_to_attractions_blocks = SliderSection(driver)
        scroll_to_attractions_blocks.scroll_to_attractions_blocks()
        check_the_attractions_block = SliderSection(driver)
        check_the_attractions_block.check_the_attractions_block()
        check_the_all_container_attraction = SliderSection(driver)
        check_the_all_container_attraction.check_the_all_container_attraction()
        click_next_and_check_container_all_container = SliderSection(driver)
        click_next_and_check_container_all_container.click_next_and_check_container_all_container()
        click_next_again_and_check_container_all_container = SliderSection(driver)
        click_next_again_and_check_container_all_container.click_next_again_and_check_container_all_container()

    def test_hotel_slider_option(self, driver):
        driver.get(TestData.URL)
        scroll_to_hotel_sliders = SliderSection(driver)
        scroll_to_hotel_sliders.scroll_to_hotel_sliders()
        check_the_hotel_container = SliderSection(driver)
        check_the_hotel_container.check_the_hotel_container()
        click_next_and_check_the_container_again = SliderSection(driver)
        click_next_and_check_the_container_again.click_next_and_check_the_container_again()
        check_the_reservation_link = SliderSection(driver)
        check_the_reservation_link.check_the_reservation_link()

    def test_train_slider_option(self, driver):
        driver.get(TestData.URL)
        scroll_to_train_section = SliderSection(driver)
        scroll_to_train_section.scroll_to_train_section()
        check_the_train_container = SliderSection(driver)
        check_the_train_container.check_the_train_face_blocks()
        check_the_reservation_train_link = SliderSection(driver)
        check_the_reservation_train_link.check_the_reservation_train_link()

    def test_news_option(self, driver):
        driver.get(TestData.URL)
        scroll_to_news = SliderSection(driver)
        scroll_to_news.scroll_to_news()
        check_the_all_container_box = SliderSection(driver)
        check_the_all_container_box.check_the_all_container_box()
        check_the_each_container = SliderSection(driver)
        check_the_each_container.check_the_each_container()
        check_the_each_blocks_news = SliderSection(driver)
        check_the_each_blocks_news.check_the_each_blocks_news()
        check_the_block_links = SliderSection(driver)
        check_the_block_links.check_the_block_links()

    def test_other_delay(self, driver):
        driver.get(TestData.URL)
        scroll_to_other_delay = SliderSection(driver)
        scroll_to_other_delay.scroll_to_other_delay()
        check_other_delay_container = SliderSection(driver)
        check_other_delay_container.check_other_delay_container()
        check_each_blocks = SliderSection(driver)
        check_each_blocks.check_each_blocks()

    def test_comment_section(self, driver):
        driver.get(TestData.URL)
        scroll_to_comment = SliderSection(driver)
        scroll_to_comment.scroll_to_comment()
        check_the_comment_container = SliderSection(driver)
        check_the_comment_container.check_the_comment_container()
        check_the_write_comment_button = SliderSection(driver)
        check_the_write_comment_button.check_the_write_comment_button()
        check_and_click_navigation_arrow = SliderSection(driver)
        check_and_click_navigation_arrow.check_and_click_navigation_arrow()