import pytest
from VOTPUSK.Articles_main.articles_sliders.comment_section import CommentLocator
from VOTPUSK.Articles_main.articles_sliders.topic_blocks import TopicBlocks
from VOTPUSK.Articles_main.field_articles_forms.articles_form import ArticlesFormLocators
from VOTPUSK.Main.test.TestBase import BaseTest
from VOTPUSK.Articles_main.article_header.articles_header import ArticleHeaderLocator
from VOTPUSK.Articles_main.config.Config import TestData
from VOTPUSK.Articles_main.articles_sliders.articles_slider import ArticlesSliderLocators
from VOTPUSK.Articles_main.articles_sliders.photo_sliders import PhotoSection
from VOTPUSK.Articles_main.articles_sliders.attractions_slider import AttractionLocators
from VOTPUSK.Articles_main.articles_sliders.what_to_see import WhatToSee


class TestArticlesPage(BaseTest):
    def test_articles_header(self, driver):
        driver.get(TestData.URL)
        check_the_article_header_exist = ArticleHeaderLocator(driver)
        check_the_article_header_exist.check_the_article_header_exist()

    @pytest.mark.smoke
    def test_check_container_articles_forms(self, driver):
        driver.get(TestData.URL)
        scroll_to_locator = ArticlesFormLocators(driver)
        scroll_to_locator.scroll_to_locator()
        assert_container_country = ArticlesFormLocators(driver)
        assert_container_country.assert_container_country()
        select_random_randint_country = ArticlesFormLocators(driver)
        select_random_randint_country.select_random_randint_country()
        assert_container_cities = ArticlesFormLocators(driver)
        assert_container_cities.assert_container_cities()
        select_random_randint_cities = ArticlesFormLocators(driver)
        select_random_randint_cities.select_random_randint_cities()
        assert_container_themes = ArticlesFormLocators(driver)
        assert_container_themes.assert_container_themes()
        select_random_randint_themes = ArticlesFormLocators(driver)
        select_random_randint_themes.select_random_randint_themes()

    @pytest.mark.smoke
    def test_topics_theme(self, driver):
        driver.get(TestData.URL)
        scroll_into_view = ArticlesSliderLocators(driver)
        scroll_into_view.scroll_into_view()
        assert_al_topics_present = ArticlesSliderLocators(driver)
        assert_al_topics_present.assert_al_topics_present()
        check_the_wrapper_container = ArticlesSliderLocators(driver)
        check_the_wrapper_container.check_the_wrapper_container()

    @pytest.mark.smoke
    def test_news_slider(self, driver):
        driver.get(TestData.URL)
        scroll_to_new_articles_page = ArticlesSliderLocators(driver)
        scroll_to_new_articles_page.scroll_to_new_articles_page()
        assert_navigation_link = ArticlesSliderLocators(driver)
        assert_navigation_link.assert_navigation_link()
        click_to_prev_navigation_arrow = ArticlesSliderLocators(driver)
        click_to_prev_navigation_arrow.click_to_prev_navigation_arrow()
        assert_1_2_blocks_in_articles_container = ArticlesSliderLocators(driver)
        assert_1_2_blocks_in_articles_container.assert_1_2_blocks_in_articles_container()
        assert_3_4_blocks_in_articles_container = ArticlesSliderLocators(driver)
        assert_3_4_blocks_in_articles_container.assert_3_4_blocks_in_articles_container()
        assert_read_more_links_1_2 = ArticlesSliderLocators(driver)
        assert_read_more_links_1_2.assert_read_more_links_1_2()
        assert_read_more_links_3_4 = ArticlesSliderLocators(driver)
        assert_read_more_links_3_4.assert_read_more_links_3_4()
        assert_target_blank_1_2 = ArticlesSliderLocators(driver)
        assert_target_blank_1_2.assert_target_blank_1_2()
        assert_target_blank_3_4 = ArticlesSliderLocators(driver)
        assert_target_blank_3_4.assert_target_blank_3_4()
        assert_presence_art_nav_arrow = ArticlesSliderLocators(driver)
        assert_presence_art_nav_arrow.assert_presence_art_nav_arrow()
        click_twice_article_next_blocks = ArticlesSliderLocators(driver)
        click_twice_article_next_blocks.click_twice_article_next_blocks()
        assert_all_item_articles_blocks_1_2 = ArticlesSliderLocators(driver)
        assert_all_item_articles_blocks_1_2.assert_all_item_articles_blocks_1_2()
        assert_all_item_articles_blocks_3_4 = ArticlesSliderLocators(driver)
        assert_all_item_articles_blocks_3_4.assert_all_item_articles_blocks_3_4()
        assert_more_links_next_1_2 = ArticlesSliderLocators(driver)
        assert_more_links_next_1_2.assert_more_links_next_1_2()
        assert_more_links_next_3_4 = ArticlesSliderLocators(driver)
        assert_more_links_next_3_4.assert_more_links_next_3_4()
        assert_target_blanks_next_1_2 = ArticlesSliderLocators(driver)
        assert_target_blanks_next_1_2.assert_target_blanks_next_1_2()
        assert_target_blanks_next_3_4 = ArticlesSliderLocators(driver)
        assert_target_blanks_next_3_4.assert_target_blanks_next_3_4()
        assert_nav_upper_arrow = ArticlesSliderLocators(driver)
        assert_nav_upper_arrow.assert_nav_upper_arrow()
        click_twice_article_next_blocks_upper = ArticlesSliderLocators(driver)
        click_twice_article_next_blocks_upper.click_twice_article_next_blocks_upper()
        check_the_each_upper_article_blocks_1_2 = ArticlesSliderLocators(driver)
        check_the_each_upper_article_blocks_3_4 = ArticlesSliderLocators(driver)
        check_the_each_upper_article_blocks_3_4.check_the_each_upper_article_blocks_3_4()
        assert_read_more_article_links_upper_1_2 = ArticlesSliderLocators(driver)
        assert_read_more_article_links_upper_1_2.assert_read_more_article_links_upper_1_2()
        assert_read_more_article_links_upper_3_4 = ArticlesSliderLocators(driver)
        assert_read_more_article_links_upper_3_4.assert_read_more_article_links_upper_3_4()
        assert_articles_target_blank_upper_1_2 = ArticlesSliderLocators(driver)
        assert_articles_target_blank_upper_1_2.assert_articles_target_blank_upper_1_2()
        assert_articles_target_blank_upper_3_4 = ArticlesSliderLocators(driver)
        assert_articles_target_blank_upper_3_4.assert_articles_target_blank_upper_3_4()

    @pytest.mark.smoke
    def test_hotel_section(self, driver):
        driver.get(TestData.URL)
        scroll_to_popular_articles_section = ArticlesSliderLocators(driver)
        scroll_to_popular_articles_section.scroll_to_popular_articles_section()
        check_each_element_locator_null = ArticlesSliderLocators(driver)
        check_each_element_locator_null.check_each_element_locator_null()
        assert_navigation_arrow = ArticlesSliderLocators(driver)
        assert_navigation_arrow.assert_navigation_arrow()
        click_to_next_locator_slider_once = ArticlesSliderLocators(driver)
        click_to_next_locator_slider_once.click_to_next_locator_slider_once()
        check_each_element_locator_once = ArticlesSliderLocators(driver)
        check_each_element_locator_once.check_each_element_locator_once()
        assert_navigation_arrow_back = ArticlesSliderLocators(driver)
        assert_navigation_arrow_back.assert_navigation_arrow_back()
        click_to_next_locator_slider_twice = ArticlesSliderLocators(driver)
        click_to_next_locator_slider_twice.click_to_next_locator_slider_twice()
        check_each_element_locator_twice = ArticlesSliderLocators(driver)
        check_each_element_locator_twice.check_each_element_locator_twice()
        assert_navigation_arrow_third = ArticlesSliderLocators(driver)
        assert_navigation_arrow_third.assert_navigation_arrow_third()
        click_to_next_locator_slider_thirds = ArticlesSliderLocators(driver)
        click_to_next_locator_slider_thirds.click_to_next_locator_slider_thirds()
        check_each_element_locator_thirds = ArticlesSliderLocators(driver)
        check_each_element_locator_thirds.check_each_element_locator_thirds()
        assert_navigation_arrow_fourth = ArticlesSliderLocators(driver)
        assert_navigation_arrow_fourth.assert_navigation_arrow_fourth()
        click_to_next_locator_slider_fourths = ArticlesSliderLocators(driver)
        click_to_next_locator_slider_fourths.click_to_next_locator_slider_fourths()
        check_each_element_locator_fourths = ArticlesSliderLocators(driver)
        check_each_element_locator_fourths.check_each_element_locator_fourths()

    @pytest.mark.smoke
    def test_photo(self, driver):
        driver.get(TestData.URL)
        scroll_to_photo = PhotoSection(driver)
        scroll_to_photo.scroll_to_photo()
        assert_full_container = PhotoSection(driver)
        assert_full_container.assert_full_container()
        assert_dropdown = PhotoSection(driver)
        assert_dropdown.assert_dropdown()

    @pytest.mark.smoke
    def test_new_attractions_sections(self, driver):
        driver.get(TestData.URL)
        scroll_to_attractions_section = AttractionLocators(driver)
        scroll_to_attractions_section.scroll_to_attractions_section()
        click_to_prev_navigation_arrow = AttractionLocators(driver)
        click_to_prev_navigation_arrow.click_to_prev_navigation_arrow()
        assert_attractions_blocks_1 = AttractionLocators(driver)
        assert_attractions_blocks_1.assert_attractions_blocks_1()
        assert_attractions_blocks_2 = AttractionLocators(driver)
        assert_attractions_blocks_2.assert_attractions_blocks_2()
        assert_attractions_blocks_3 = AttractionLocators(driver)
        assert_attractions_blocks_3.assert_attractions_blocks_3()
        assert_attractions_blocks_4 = AttractionLocators(driver)
        assert_attractions_blocks_4.assert_attractions_blocks_4()
        assert_navigation_arrow_next = AttractionLocators(driver)
        assert_navigation_arrow_next.assert_navigation_arrow_next()
        double_click_to_navigation = AttractionLocators(driver)
        double_click_to_navigation.double_click_to_navigation()
        assert_attractions_blocks_5 = AttractionLocators(driver)
        assert_attractions_blocks_5.assert_attractions_blocks_5()
        assert_attractions_blocks_6 = AttractionLocators(driver)
        assert_attractions_blocks_6.assert_attractions_blocks_6()
        assert_attractions_blocks_7 = AttractionLocators(driver)
        assert_attractions_blocks_7.assert_attractions_blocks_7()
        assert_attractions_blocks_8 = AttractionLocators(driver)
        assert_attractions_blocks_8.assert_attractions_blocks_8()

    @pytest.mark.smoke
    def test_all_topics(self, driver):
        driver.get(TestData.URL)
        scroll_to_all_topics_section = TopicBlocks(driver)
        scroll_to_all_topics_section.scroll_to_all_topics_section()
        check_the_topics_container = TopicBlocks(driver)
        check_the_topics_container.check_the_topics_container()
        click_to_open_more_button = TopicBlocks(driver)
        click_to_open_more_button.click_to_open_more_button()
        check_the_footer_menu = TopicBlocks(driver)
        check_the_footer_menu.check_the_footer_menu()
        check_each_block_offer = TopicBlocks(driver)
        check_each_block_offer.check_each_block_offer()

    @pytest.mark.smoke
    def test_what_to_see(self, driver):
        driver.get(TestData.URL)
        scroll_to_desktop_item_blocks = WhatToSee(driver)
        scroll_to_desktop_item_blocks.scroll_to_desktop_item_blocks()
        check_visibility_blocks = WhatToSee(driver)
        check_visibility_blocks.check_visibility_blocks()
        check_visibility_all_news_link = WhatToSee(driver)
        check_visibility_all_news_link.check_visibility_all_news_link()

    @pytest.mark.smoke
    def test_comment_section(self, driver):
        driver.get(TestData.URL)
        scroll_into_view = CommentLocator(driver)
        scroll_into_view.scroll_into_view()
        assert_visibility_of_container = CommentLocator(driver)
        assert_visibility_of_container.assert_visibility_of_container()
        assert_text_area = CommentLocator(driver)
        assert_text_area.assert_text_area()
        assert_like_area = CommentLocator(driver)
        assert_like_area.assert_like_area()
        assert_how_more_options = CommentLocator(driver)
        assert_how_more_options.assert_how_more_options()
        assert_element_clickable = CommentLocator(driver)
        assert_element_clickable.assert_element_clickable()
        assert_ad_block = CommentLocator(driver)
        assert_ad_block.assert_ad_block()
