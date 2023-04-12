import pytest
from VOTPUSK.Main.Header.header_info import HeaderLocators
from VOTPUSK.Main.Config.TestData import TestData
from VOTPUSK.Main.Title.title import TitleLocator
from VOTPUSK.Main.test.TestBase import BaseTest
from VOTPUSK.Main.FieldForms_main.form_section import ToursFormLocators
from VOTPUSK.Main.Sliders.sliders_section import SliderSection


class TestPage(BaseTest):
    @pytest.mark.smoke
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

    @pytest.mark.smoke
    def test_typeSection(self, driver):
        driver.get(TestData.URL)
        section = ToursFormLocators(driver)
        section.type_section()

    @pytest.mark.smoke
    def test_russian_tour(self, driver):
        driver.get(TestData.URL)
        scroll_to_keys = ToursFormLocators(driver)
        scroll_to_keys.scroll_to_keys()
        form_keys = ToursFormLocators(driver)
        form_keys.form_keys()
        check_the_len_list = ToursFormLocators(driver)
        check_the_len_list.check_the_len_list()
        type_attraction = ToursFormLocators(driver)
        type_attraction.type_attraction()
        check_the_attractions_container = ToursFormLocators(driver)
        check_the_attractions_container.check_the_attractions_container()
        do_random_click = ToursFormLocators(driver)
        do_random_click.do_random_click()
        do_double_click_calendar = ToursFormLocators(driver)
        do_double_click_calendar.do_double_click_calendar()
        do_random_choice_date = ToursFormLocators(driver)
        do_random_choice_date.do_random_choice_date()
        do_random_choice_next = ToursFormLocators(driver)
        do_random_choice_next.do_random_choice_next()
        is_exist = ToursFormLocators(driver)
        is_exist.is_exist()

    @pytest.mark.smoke
    def test_world_tour(self, driver):
        driver.get(TestData.URL)
        world_tour_switcher = ToursFormLocators(driver)
        world_tour_switcher.world_tour_switcher()
        world_tour_input_form = ToursFormLocators(driver)
        world_tour_input_form.world_tour_input_form()
        check_words_tour_len_list = ToursFormLocators(driver)
        check_words_tour_len_list.check_words_tour_len_list()
        witch_to_next_input_form = ToursFormLocators(driver)
        witch_to_next_input_form.witch_to_next_input_form()
        send_keys_to_next_input_form = ToursFormLocators(driver)
        send_keys_to_next_input_form.send_keys_to_next_input_form()
        scroll_to_world_tour = ToursFormLocators(driver)
        scroll_to_world_tour.scroll_to_world_tour()
        assert_calendar_enabled = ToursFormLocators(driver)
        assert_calendar_enabled.assert_calendar_enabled()
        random_randint_choice = ToursFormLocators(driver)
        random_randint_choice.random_randint_choice()
        click_and_assert_modal_enabled = ToursFormLocators(driver)
        click_and_assert_modal_enabled.click_and_assert_modal_enabled()
        random_randint_input_signs = ToursFormLocators(driver)
        random_randint_input_signs.random_randint_input_signs()
        check_visibility_tourist_quantity_modal = ToursFormLocators(driver)
        check_visibility_tourist_quantity_modal.check_visibility_tourist_quantity_modal()
        click_to_quantity_modal = ToursFormLocators(driver)
        click_to_quantity_modal.click_to_quantity_modal()
        assert_kids_quantity = ToursFormLocators(driver)
        assert_kids_quantity.assert_kids_quantity()
        random_randint_click_kids_choice = ToursFormLocators(driver)
        random_randint_click_kids_choice.random_randint_click_kids_choice()
        check_the_blocks_add_buttons = ToursFormLocators(driver)
        check_the_blocks_add_buttons.check_the_blocks_add_buttons()

    @pytest.mark.smoke
    def test_hotel_options(self, driver):
        driver.get(TestData.URL)
        switch_to_hotels = ToursFormLocators(driver)
        switch_to_hotels.switch_to_hotels()
        scroll_page_into_view = ToursFormLocators(driver)
        scroll_page_into_view.scroll_page_into_view()
        do_send_keys_hotel = ToursFormLocators(driver)
        do_send_keys_hotel.do_send_keys_hotel()
        do_click_on_check_in_option = ToursFormLocators(driver)
        do_click_on_check_in_option.do_click_on_check_in_option()
        wait_until_widget_loaded = ToursFormLocators(driver)
        wait_until_widget_loaded.wait_until_widget_loaded()
        randint_click_to_check_in = ToursFormLocators(driver)
        randint_click_to_check_in.randint_click_to_check_in()
        open_dropdown_quantity = ToursFormLocators(driver)
        open_dropdown_quantity.open_dropdown_quantity()
        random_randint_click_adults_opt = ToursFormLocators(driver)
        random_randint_click_adults_opt.random_randint_click_adults_opt()
        open_dropdown_kids = ToursFormLocators(driver)
        open_dropdown_kids.open_dropdown_kids()
        select_widget_item = ToursFormLocators(driver)
        select_widget_item.select_widget_item()
        check_visibility_search_button = ToursFormLocators(driver)
        check_visibility_search_button.check_visibility_search_button()
        check_visibility_search_button = ToursFormLocators(driver)
        check_visibility_search_button.check_visibility_search_button()

    @pytest.mark.smoke
    def test_train_options(self, driver):
        driver.get(TestData.URL)
        switch_to_train = ToursFormLocators(driver)
        switch_to_train.switch_to_train_option()
        do_send_keys_to_form_from = ToursFormLocators(driver)
        do_send_keys_to_form_from.do_send_keys_to_input_form_from()
        do_send_keys_to_form_to = ToursFormLocators(driver)
        do_send_keys_to_form_to.do_send_keys_to_input_form_to()
        scroll_page_into_element_view = ToursFormLocators(driver)
        scroll_page_into_element_view.scroll_page_into_element_view()
        do_click_to_calendar_option = ToursFormLocators(driver)
        do_click_to_calendar_option.do_click_to_calendar_option()
        do_random_choice_to_calendar_date = ToursFormLocators(driver)
        do_random_choice_to_calendar_date.do_random_choice_calendar_date()
        do_check_search_button = ToursFormLocators(driver)
        do_check_search_button.do_check_search_button_visibility()

    @pytest.mark.smoke
    def test_routs_option(self, driver):
        driver.get(TestData.URL)
        do_switch_to_routs = ToursFormLocators(driver)
        do_switch_to_routs.do_switch_to_routs()
        do_send_keys_routs_first = ToursFormLocators(driver)
        do_send_keys_routs_first.do_send_keys_routs_first()
        assert_routs_from_len_list = ToursFormLocators(driver)
        assert_routs_from_len_list.assert_routs_from_len_list()
        do_send_keys_routs_second = ToursFormLocators(driver)
        do_send_keys_routs_second.do_send_keys_routs_second()
        assert_routs_to_len_list = ToursFormLocators(driver)
        assert_routs_to_len_list.assert_routs_to_len_list()
        do_check_search_routs_button = ToursFormLocators(driver)
        do_check_search_routs_button.do_check_search_routs_button()

    @pytest.mark.smoke
    def test_country_And_cities(self, driver):
        driver.get(TestData.URL)
        switch_option = ToursFormLocators(driver)
        switch_option.switch_to_country_and_cities_option()
        check_the_total_form_and_click = ToursFormLocators(driver)
        check_the_total_form_and_click.check_the_total_form()
        random_select_country = ToursFormLocators(driver)
        random_select_country.random_select_country()
        random_select_city = ToursFormLocators(driver)
        random_select_city.random_select_city()
        random_select_cities = ToursFormLocators(driver)
        random_select_cities.random_select_cities_and_check_the_search_button()

    @pytest.mark.smoke
    def test_tours_wrapper(self, driver):
        driver.get(TestData.URL)
        check_wrapper = SliderSection(driver)
        check_wrapper.do_check_block_tours_option()

    @pytest.mark.smoke
    def test_tours_slider(self, driver):
        driver.get(TestData.URL)
        scroll_page_into_view_tours = SliderSection(driver)
        scroll_page_into_view_tours.scroll_page_into_view_tours()
        assert_articles_container = SliderSection(driver)
        assert_articles_container.assert_articles_container()
        do_check_block_tours_option = SliderSection(driver)
        do_check_block_tours_option.do_check_block_tours_option()
        check_tour_container = SliderSection(driver)
        check_tour_container.check_tour_container()
        check_each_blocks_to_exist_tours_first = SliderSection(driver)
        check_each_blocks_to_exist_tours_first.check_each_blocks_to_exist_tours_first()
        check_each_blocks_to_exist = SliderSection(driver)
        check_each_blocks_to_exist.check_each_blocks_to_exist()
        check_tour_container_again = SliderSection(driver)
        check_tour_container_again.check_tour_container_again()
        switch_tour_section = SliderSection(driver)
        switch_tour_section.switch_tour_section()
        check_the_container_inside = SliderSection(driver)
        check_the_container_inside.check_the_container_inside()
        slide_to_next_blocks = SliderSection(driver)
        slide_to_next_blocks.slide_to_next_blocks()

    @pytest.mark.smoke
    def test_articles_container(self, driver):
        driver.get(TestData.URL)
        scroll_to_page_articles = SliderSection(driver)
        scroll_to_page_articles.scroll_to_page_articles()
        check_the_block_first_container = SliderSection(driver)
        check_all_item_container = SliderSection(driver)
        check_all_item_container.check_all_item_container()
        assert_articles_container = SliderSection(driver)
        assert_articles_container.assert_articles_container()
        check_all_article_item = SliderSection(driver)
        check_all_article_item.check_all_article_item()
        check_form_block = SliderSection(driver)
        check_form_block.check_form_block()
        assert_page_loaded = SliderSection(driver)
        assert_page_loaded.assert_page_loaded()
        random_select_country = SliderSection(driver)
        random_select_country.random_select_country()
        random_randint_cities = SliderSection(driver)
        random_randint_cities.random_randint_cities()
        random_select_themes = SliderSection(driver)
        random_select_themes.random_select_themes()
        assert_look_after_link = SliderSection(driver)
        assert_look_after_link.assert_look_after_link()
        check_articles_search_button = SliderSection(driver)
        check_articles_search_button.check_articles_search_button()

    @pytest.mark.smoke
    def test_attractions_container(self, driver):
        driver.get(TestData.URL)
        scroll_to_attractions_blocks = SliderSection(driver)
        scroll_to_attractions_blocks.scroll_to_attractions_blocks()
        check_the_attractions_block = SliderSection(driver)
        check_the_attractions_block.check_the_attractions_block()
        check_the_all_container_attraction = SliderSection(driver)
        check_the_all_container_attraction.check_the_all_container_attraction()
        assert_click_navigation_arrow = SliderSection(driver)
        assert_click_navigation_arrow.assert_click_navigation_arrow()
        assert_attraction_container = SliderSection(driver)
        assert_attraction_container.assert_attraction_container()
        click_next_again_and_check_container_all_container = SliderSection(driver)
        click_next_again_and_check_container_all_container.click_next_again_and_check_container_all_container()

    @pytest.mark.smoke
    def test_hotel_slider_option(self, driver):
        driver.get(TestData.URL)
        scroll_to_hotel_sliders = SliderSection(driver)
        scroll_to_hotel_sliders.scroll_to_hotel_sliders()
        check_the_hotel_container = SliderSection(driver)
        check_the_hotel_container.check_the_hotel_container()
        move_next_slide = SliderSection(driver)
        move_next_slide.move_next_slide()
        assert_hotel_container = SliderSection(driver)
        assert_hotel_container.assert_hotel_container()
        check_the_reservation_link = SliderSection(driver)
        check_the_reservation_link.check_the_reservation_link()

    @pytest.mark.smoke
    def test_train_slider_option(self, driver):
        driver.get(TestData.URL)
        scroll_to_train_section = SliderSection(driver)
        scroll_to_train_section.scroll_to_train_section()
        """check_the_train_face_blocks = SliderSection(driver)
        check_the_train_face_blocks.check_the_train_face_blocks()
        move_next_train_slide = SliderSection(driver)
        move_next_train_slide.move_next_train_slide()
        move_next_train_slider = SliderSection(driver)
        move_next_train_slider.move_next_train_slider()"""
        check_the_reservation_train_link = SliderSection(driver)
        check_the_reservation_train_link.check_the_reservation_train_link()

    @pytest.mark.smoke
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

    @pytest.mark.smoke
    def test_other_delay(self, driver):
        driver.get(TestData.URL)
        scroll_to_other_delay = SliderSection(driver)
        scroll_to_other_delay.scroll_to_other_delay()
        check_other_delay_container = SliderSection(driver)
        check_other_delay_container.check_other_delay_container()
        assert_avia_block = SliderSection(driver)
        assert_avia_block.assert_avia_block()
        assert_excursion_block = SliderSection(driver)
        assert_excursion_block.assert_excursion_block()
        assert_insurance_block = SliderSection(driver)
        assert_insurance_block.assert_insurance_block()
        assert_transfer_block = SliderSection(driver)
        assert_transfer_block.assert_transfer_block()
        assert_autobus_block = SliderSection(driver)
        assert_autobus_block.assert_autobus_block()
        assert_auto_rent = SliderSection(driver)
        assert_auto_rent.assert_auto_rent()

    @pytest.mark.smoke
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