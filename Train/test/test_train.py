from VOTPUSK.Train.train_form.train_schandual import TrainCheckingTrainLocators
from VOTPUSK.Train.sliders.sliders import SlidersTrainLocator
from VOTPUSK.Train.test.testbase import BaseTest
from VOTPUSK.Train.config.configuration import TestData


class TestTrain(BaseTest):

    def test_schedule_form(self, driver):
        driver.get(TestData.URL)
        assert_schedule_button = TrainCheckingTrainLocators(driver)
        assert_schedule_button.assert_schedule_button()
        assert_by_routs_form = TrainCheckingTrainLocators(driver)
        assert_by_routs_form.assert_by_routs_form()
        assert_by_routs_form_to = TrainCheckingTrainLocators(driver)
        assert_by_routs_form_to.assert_by_routs_form_to()
        assert_select_random_date_day = TrainCheckingTrainLocators(driver)
        assert_select_random_date_day.assert_select_random_date_day()
        assert_select_random_date_month = TrainCheckingTrainLocators(driver)
        assert_select_random_date_month.assert_select_random_date_month()
        assert_select_random_date_year = TrainCheckingTrainLocators(driver)
        assert_select_random_date_year.assert_select_random_date_year()
        assert_search_by_routs_button = TrainCheckingTrainLocators(driver)
        assert_search_by_routs_button.assert_search_by_routs_button()

    def test_by_station(self, driver):
        driver.get(TestData.URL)
        assert_click_by_station_button = TrainCheckingTrainLocators(driver)
        assert_click_by_station_button.assert_click_by_station_button()
        assert_by_station_input = TrainCheckingTrainLocators(driver)
        assert_by_station_input.assert_by_station_input()
        assert_select_random_date_station_day = TrainCheckingTrainLocators(driver)
        assert_select_random_date_station_day.assert_select_random_date_station_day()
        assert_select_random_date_station_month = TrainCheckingTrainLocators(driver)
        assert_select_random_date_station_month.assert_select_random_date_station_month()
        assert_select_random_date_station_year = TrainCheckingTrainLocators(driver)
        assert_select_random_date_station_year.assert_select_random_date_station_year()
        assert_station_search_button = TrainCheckingTrainLocators(driver)
        assert_station_search_button.assert_station_search_button()

    def test_train_by_number(self, driver):
        driver.get(TestData.URL)
        assert_by_train_number = TrainCheckingTrainLocators(driver)
        assert_by_train_number.assert_by_train_number()
        assert_search_by_number_form = TrainCheckingTrainLocators(driver)
        assert_search_by_number_form.assert_search_by_number_form()

    def test_obtain_tickets(self, driver):
        driver.get(TestData.URL)
        assert_obtain_button = TrainCheckingTrainLocators(driver)
        assert_obtain_button.assert_obtain_button()
        assert_click_obtain_tickets = TrainCheckingTrainLocators(driver)
        assert_click_obtain_tickets.assert_click_obtain_tickets()
        assert_obtain_form = TrainCheckingTrainLocators(driver)
        assert_obtain_form.assert_obtain_form()
        assert_obtain_to = TrainCheckingTrainLocators(driver)
        assert_obtain_to.assert_obtain_to()
        assert_select_randomly_date_from = TrainCheckingTrainLocators(driver)
        assert_select_randomly_date_from.assert_select_randomly_date_from()
        assert_obtain_next_date = TrainCheckingTrainLocators(driver)
        assert_obtain_next_date.assert_obtain_next_date()
        assert_select_randomly_date_to = TrainCheckingTrainLocators(driver)
        assert_select_randomly_date_to.assert_select_randomly_date_to()
        assert_obtain_search_button = TrainCheckingTrainLocators(driver)
        assert_obtain_search_button.assert_obtain_search_button()

    # Популярные направления
    def test_popular_destination(self, driver):
        driver.get(TestData.URL)
        assert_scroll_into_view_popular_destination = SlidersTrainLocator(driver)
        assert_scroll_into_view_popular_destination.assert_scroll_into_view_popular_destination()
        assert_popular_destination_block = SlidersTrainLocator(driver)
        assert_popular_destination_block.assert_popular_destination_block()
        assert_cities_blocks = SlidersTrainLocator(driver)
        assert_cities_blocks.assert_cities_blocks()
        assert_arrow_links = SlidersTrainLocator(driver)
        assert_arrow_links.assert_arrow_links()
        assert_show_all_destination_link = SlidersTrainLocator(driver)
        assert_show_all_destination_link.assert_show_all_destination_link()

    def test_obtain_tickets_module(self, driver):
        driver.get(TestData.URL)
        assert_scroll_into_view_obtain_tickets = SlidersTrainLocator(driver)
        assert_scroll_into_view_obtain_tickets.assert_scroll_into_view_obtain_tickets()
        assert_train_blocks = SlidersTrainLocator(driver)
        assert_train_blocks.assert_train_blocks()
        assert_read_obtain_tickets_links = SlidersTrainLocator(driver)
        assert_read_obtain_tickets_links.assert_read_obtain_tickets_links()

    def test_comment_section(self, driver):
        driver.get(TestData.URL)
        assert_scroll_into_view_comment_section = SlidersTrainLocator(driver)
        assert_scroll_into_view_comment_section.assert_scroll_into_view_comment_section()
        assert_comment_section = SlidersTrainLocator(driver)
        assert_comment_section.assert_comment_section()
        assert_write_comment_button = SlidersTrainLocator(driver)
        assert_write_comment_button.assert_write_comment_button()

    def test_faq_module(self, driver):
        driver.get(TestData.URL)
        assert_scroll_into_view_faq = SlidersTrainLocator(driver)
        assert_scroll_into_view_faq.assert_scroll_into_view_faq()
        assert_faq_block = SlidersTrainLocator(driver)
        assert_faq_block.assert_faq_block()
        assert_show_all_section = SlidersTrainLocator(driver)
        assert_show_all_section.assert_show_all_section()

