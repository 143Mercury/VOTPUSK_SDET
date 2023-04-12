import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from VOTPUSK.BaseMethods.object_methods import BaseMethods


class SliderSection(BaseMethods):
    # Опция выбора типы опций
    BLOCK_VACATION_TYPE_WRAPPER = (By.CSS_SELECTOR, '[class="vacations-type__wrapper"]')

    TOURS_ALL_ITEM_CONTAINER = (By.CSS_SELECTOR, '[class="tours__banner "]')

    FIRST_TOUR_BLOCK = (By.CSS_SELECTOR, '[alt="в Адыгею"]')
    SECOND_TOUR_BLOCK = (By.CSS_SELECTOR, '[alt="на Байкал"]')
    THIRD_TOUR_BLOCK = (By.CSS_SELECTOR, '[alt="в Дагестан"]')

    FOURTH_TOUR_BLOCK = (By.XPATH, '//*[@id="swiper-wrapper-0549c746f0e4c691"]/div[3]/a[1]/picture/img'),
    FIFTH_TOUR_BLOCK = (By.XPATH, '//*[@id="swiper-wrapper-0549c746f0e4c691"]/div[3]/a[2]/picture/img'),
    SIXTH_TOUR_BLOCK = (By.XPATH, '//*[@id="swiper-wrapper-0549c746f0e4c691"]/div[3]/a[3]/picture/img'),

    TOURS_SLIDER_NEXT = (By.XPATH, '/html/body/section[5]/div/div/div/div[1]/div[3]')
    TOURS_SLIDER_WORLD_NEXT = (By.XPATH, '/html/body/section[5]/div/div/div/div[2]/div[3]')
    TOURS_SLIDER_PREV = (By.XPATH, '/html/body/section[5]/div/div/div/div[1]/div[2]')
    TOUR_SWITCHER = (By.CSS_SELECTOR, '[class="tours__switcher"]')
    CHECK_THE_ORDER_FUNCTION = (By.CSS_SELECTOR, '[class="tours__order tours__order_active"]')

    # Статьи о путешествиях
    ARTICLE_CONTAINER = (By.CSS_SELECTOR, '[class="articles__banner "]')

    ARTICLE_BLOCK_FIRST = (By.XPATH, '//*[@id="swiper-wrapper-b87918c6e510adf4"]/div[10]/a/picture/img')
    ARTICLE_BLOCK_SECOND = (By.XPATH, '//*[@id="swiper-wrapper-8b5aa897f2573780"]/div[11]/a/picture/img')
    ARTICLE_BLOCK_THIRD = (By.XPATH, '//*[@id="swiper-wrapper-8b5aa897f2573780"]/div[12]/a/picture/img')

    ARTICLES_SLIDERS_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next articles__slider_next"]')
    ARTICLES_SLIDERS_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev articles__slider_prev"]')
    CHECK_ALL_ARTICLES_ITEM = (By.XPATH, '/html/body/section[6]/div/div/div/div[3]/a')
    # Форма поиска статей
    FIELD_FORM_BLOCK = (By.CSS_SELECTOR, '[class="articles__search"]')

    OPEN_CONTAINER_COUNTRY = (By.CSS_SELECTOR, '[id="select2-country-container"]')
    CONTAINER_COUNTRY_CITY_THEMES = (By.CSS_SELECTOR, '[class="select2-results"]')
    OPEN_CONTAINER_CITIES = (By.CSS_SELECTOR, '[id="select2-city-container"]')
    CONTAINER_CITIES = (By.CSS_SELECTOR, '')
    OPEN_CONTAINER_THEMES = (By.CSS_SELECTOR, '[id="select2-theme-container"]')

    SEARCH_ALL_ARTICLES_LINK = (By.CSS_SELECTOR, '[class="articles__order-redirect"]')

    SEARCH_ARTICLES_BUTTON = (By.CSS_SELECTOR, '[class="articles__search-btn"]')

    # Незабываемые достопримечательности
    ATTRACTION_CONTAINER = (By.XPATH, '/html/body/section[7]/div')
    ATTRACTION_CONTAINER_BLOCK = (By.CSS_SELECTOR, '[class="places__slider swiper swiper-initialized '
                                                   'swiper-horizontal swiper-pointer-events"]')
    ATTRACTION_SLIDER_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next places__slider_next"]')
    ATTRACTION_SLIDER_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev places__slider_prev"]')

    ALL_ATTRACTIONS_ITEM = (By.CSS_SELECTOR, '[class="places__order"]')

    # Отели
    HOTEL_CONTAINER = (By.CSS_SELECTOR, '[class="container container_hotels"]')
    HOTEL_SLIDER_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next hotels__slider_next"]')
    HOTEL_SLIDER_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev hotels__slider_prev"]')
    HOTEL_BOOKING_ITEM = (By.CSS_SELECTOR, '[class="hotels__order"]')

    # ЖД билеты
    CONTAINER_TRAINS_LINK = (By.CSS_SELECTOR, '[class="tickets__order-redirect"]')
    CONTAINER_TRAINS_SLIDER_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next tickets__slider_next"]')
    CONTAINER_TRAINS_SLIDER_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev tickets__slider_prev"]')
    TRAIN_BLOCKS_0 = (By.XPATH, '//*[@id="swiper-wrapper-2c0f8045bc3ea09d"]/a[5]/picture/img')
    TRAIN_BLOCKS_1 = (By.XPATH, '//*[@id="swiper-wrapper-2c0f8045bc3ea09d"]/a[6]/picture/img')
    TRAIN_BLOCKS_2 = (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[7]/picture/img')
    TRAIN_BLOCKS_3 = (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[8]/picture/img')
    TRAIN_BLOCKS_4 = (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[9]/picture/img')
    TRAIN_BLOCKS_5 = (By.XPATH, '//*[@id="swiper-wrapper-99eb585c299ca610d"]/a[10]/picture/img')
    TRAIN_BLOCKS_6 = (By.XPATH, '//*[@id="swiper-wrapper-99eb585c299ca610d"]/a[11]/picture/img')

    # Новости - Фоторепортажи - Калейдоскоп
    CONTAINER_ITEM_NEWS_PHOTO = (By.XPATH, '/html/body/article/div')
    GALLERY_NEWS = (By.CSS_SELECTOR, '[class="gallery__news news"]')
    GALLERY_PHOTOS = (By.CSS_SELECTOR, '[class="gallery__photos photos"]')
    GALLERY_SCOPES = (By.CSS_SELECTOR, '[class="gallery__kaleidoscopes kaleidoscopes"]')
    NEWS_BLOCK_CONTAINER = (By.CSS_SELECTOR, '[class="news__wrapper"]')
    PHOTOS_BLOCK_CONTAINER = (By.CSS_SELECTOR, '[class="photos__wrapper"]')
    SCOPES_BLOCK_CONTAINER = (By.CSS_SELECTOR, '[class="kaleidoscopes__wrapper"]')

    UNDER_CONTAINER_ITEMS = (By.CSS_SELECTOR, '[class="gallery__order-redirect"]')

    # Другие услуги
    CONTAINER_OTHER_DELAY = (By.CSS_SELECTOR, '[class="other-services__wrapper"]')
    BLOCK_AVIA = (By.XPATH, '/html/body/section[10]/div/div/a[1]')
    BLOCK_EXCURSION = (By.XPATH, '/html/body/section[10]/div/div/a[2]')
    BLOCK_INSURANCE = (By.XPATH, '/html/body/section[10]/div/div/a[3]')
    BLOCK_TRANSFERS = (By.XPATH, '/html/body/section[10]/div/div/a[4]')
    BLOCK_AUTOBUS = (By.XPATH, '/html/body/section[10]/div/div/a[5]')
    BLOCK_AUTO_RENT = (By.XPATH, '/html/body/section[10]/div/div/a[6]')

    # Отзывы о Votpusk.ru
    BLOCK_COMMENT_SECTION = (By.CSS_SELECTOR, '[class="reviews__slider swiper swiper-initialized swiper-horizontal '
                                              'swiper-pointer-events"]')
    WRITE_COMMENT_BUTTON = (By.CSS_SELECTOR, '[class="reviews__btn"]')
    BLOCK_COMMENT_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next reviews__slider_next"]')
    BLOCK_COMMENT_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev reviews__slider_prev"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_page_into_view_tours(self):
        self.window_scroll_by(0, 650)
        self.sleep(2)

    def do_check_block_tours_option(self):
        self.is_element_present(SliderSection.BLOCK_VACATION_TYPE_WRAPPER)
        self.is_visible(SliderSection.BLOCK_VACATION_TYPE_WRAPPER)
        self.sleep(2)

    def check_tour_container(self):
        self.is_visible(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        self.sleep(2)

    def check_each_blocks_to_exist_tours_first(self):
        self.is_element_present(SliderSection.FIRST_TOUR_BLOCK)
        self.is_element_present(SliderSection.SECOND_TOUR_BLOCK)
        self.is_element_present(SliderSection.THIRD_TOUR_BLOCK)
        self.sleep(2)

    def check_each_blocks_to_exist(self):
        self.page_loaded(SliderSection.TOURS_SLIDER_NEXT)
        self.click_element(SliderSection.TOURS_SLIDER_NEXT)
        self.sleep(2)

    def check_tour_container_again(self):
        self.is_element_present(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        self.sleep(2)

    def switch_tour_section(self):
        self.is_element_present(SliderSection.TOUR_SWITCHER)
        self.click_element(SliderSection.TOUR_SWITCHER)
        self.sleep(2)

    def check_the_container_inside(self):
        self.page_loaded(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        self.is_element_present(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        self.sleep(2)

    def slide_to_next_blocks(self):
        self.page_loaded(SliderSection.TOURS_SLIDER_WORLD_NEXT)
        self.click_element(SliderSection.TOURS_SLIDER_WORLD_NEXT)
        self.sleep(2)

    def check_the_tour_order_button(self):
        self.is_element_present(SliderSection.CHECK_THE_ORDER_FUNCTION)
        self.sleep(2)

    # Тест формы поиска статей
    def scroll_to_page_articles(self):
        self.window_scroll_by(0, 1175)
        self.sleep(1)

    """def check_the_block_first_container(self):
        self.page_loaded(SliderSection.ARTICLE_BLOCK_FIRST)
        self.is_element_present(SliderSection.ARTICLE_BLOCK_FIRST)
        self.sleep(2)

    def check_the_blocks_second_container(self):
        self.is_element_present(SliderSection.ARTICLE_BLOCK_SECOND)
        self.sleep(2)

    def check_the_blocks_third_container(self):
        self.is_element_present(SliderSection.ARTICLE_BLOCK_THIRD)
        self.sleep(2)"""

    def check_all_item_container(self):
        self.page_loaded(SliderSection.ARTICLES_SLIDERS_NEXT)
        self.click_element(SliderSection.ARTICLES_SLIDERS_NEXT)
        self.sleep(2)

    def assert_articles_container(self): ##!
        self.page_loaded(SliderSection.ARTICLE_CONTAINER)
        self.is_element_present(SliderSection.ARTICLE_CONTAINER)
        self.sleep(2)

    def check_all_article_item(self):
        self.page_loaded(SliderSection.CHECK_ALL_ARTICLES_ITEM)
        self.is_element_present(SliderSection.CHECK_ALL_ARTICLES_ITEM)

    def check_form_block(self):
        self.page_loaded(SliderSection.FIELD_FORM_BLOCK)
        self.is_element_present(SliderSection.FIELD_FORM_BLOCK)
        self.sleep(2)

    def assert_page_loaded(self):
        self.page_loaded(SliderSection.OPEN_CONTAINER_COUNTRY)
        self.sleep(2)

    def random_select_country(self):
        self.click_element(SliderSection.OPEN_CONTAINER_COUNTRY)
        self.random_country_selection(SliderSection.CONTAINER_COUNTRY_CITY_THEMES)
        self.sleep(2)

    def random_randint_cities(self):
        self.click_element(SliderSection.OPEN_CONTAINER_CITIES)
        self.random_country_selection(SliderSection.CONTAINER_COUNTRY_CITY_THEMES)
        self.sleep(2)

    def random_select_themes(self):
        self.click_element(SliderSection.OPEN_CONTAINER_THEMES)
        self.random_country_selection(SliderSection.CONTAINER_COUNTRY_CITY_THEMES)
        self.sleep(2)

    def assert_look_after_link(self):
        self.is_element_present(SliderSection.SEARCH_ARTICLES_BUTTON)
        self.sleep(2)

    def check_articles_search_button(self):
        self.is_element_present(SliderSection.SEARCH_ALL_ARTICLES_LINK)
        self.sleep(2)

    # Достопримечательности
    def scroll_to_attractions_blocks(self):
        self.window_scroll_by(0, 1750)
        self.sleep(2)

    def check_the_attractions_block(self):
        self.is_element_present(SliderSection.ATTRACTION_CONTAINER)
        self.sleep(2)

    def check_the_all_container_attraction(self):
        self.is_element_present(SliderSection.ATTRACTION_CONTAINER_BLOCK)
        self.sleep(2)

    def assert_click_navigation_arrow(self):
        self.page_loaded(SliderSection.ATTRACTION_SLIDER_NEXT)
        self.click_element(SliderSection.ATTRACTION_SLIDER_NEXT)
        self.sleep(2)

    def assert_attraction_container(self):
        self.page_loaded(SliderSection.ATTRACTION_CONTAINER)
        self.is_element_present(SliderSection.ATTRACTION_CONTAINER)
        self.sleep(2)

    def click_next_again_and_check_container_all_container(self):
        self.page_loaded(SliderSection.ATTRACTION_SLIDER_NEXT)
        self.click_element(SliderSection.ATTRACTION_SLIDER_NEXT)
        self.is_element_present(SliderSection.ATTRACTION_CONTAINER)
        self.sleep(2)

    # Отели
    def scroll_to_hotel_sliders(self):
        self.window_scroll_by(0, 2150)
        self.sleep(2)

    def check_the_hotel_container(self):
        self.page_loaded(SliderSection.HOTEL_CONTAINER)
        self.is_element_present(SliderSection.HOTEL_CONTAINER)

    def move_next_slide(self):
        self.page_loaded(SliderSection.HOTEL_SLIDER_NEXT)
        self.click_element(SliderSection.HOTEL_SLIDER_NEXT)
        self.sleep(2)

    def assert_hotel_container(self):
        self.page_loaded(SliderSection.HOTEL_CONTAINER)
        self.is_element_present(SliderSection.HOTEL_CONTAINER)
        self.sleep(2)

    def check_the_reservation_link(self):
        self.page_loaded(SliderSection.HOTEL_BOOKING_ITEM)
        self.is_element_present(SliderSection.HOTEL_BOOKING_ITEM)
        self.sleep(2)

    # Жд билеты
    def scroll_to_train_section(self):
        self.window_scroll_by(0, 2550)
        self.sleep(2)

    """def check_the_train_face_blocks(self):
        self.page_loaded(SliderSection.TRAIN_BLOCKS_0)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_0)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_1)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_2)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_3)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_4)
        self.sleep(2)

    def move_next_train_slide(self):
        self.page_loaded(SliderSection.CONTAINER_TRAINS_SLIDER_NEXT)
        self.click_element(SliderSection.CONTAINER_TRAINS_SLIDER_NEXT)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_5)
        self.sleep(2)

    def move_next_train_slider(self):
        self.page_loaded(SliderSection.CONTAINER_TRAINS_SLIDER_NEXT)
        self.click_element(SliderSection.CONTAINER_TRAINS_SLIDER_NEXT)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_6)
        self.sleep(2)"""

    def check_the_reservation_train_link(self):
        self.page_loaded(SliderSection.CONTAINER_TRAINS_LINK)
        self.is_element_present(SliderSection.CONTAINER_TRAINS_LINK)
        self.sleep(2)

    # Новости
    def scroll_to_news(self):
        self.window_scroll_by(0, 3525)
        self.sleep(2)

    def check_the_all_container_box(self):
        self.page_loaded(SliderSection.CONTAINER_ITEM_NEWS_PHOTO)
        self.is_element_present(SliderSection.CONTAINER_ITEM_NEWS_PHOTO)
        self.sleep(2)

    def check_the_each_blocks_news(self):
        self.page_loaded(SliderSection.GALLERY_NEWS)
        self.is_element_present(SliderSection.GALLERY_NEWS)
        self.is_element_present(SliderSection.GALLERY_PHOTOS)
        self.is_element_present(SliderSection.GALLERY_SCOPES)
        self.sleep(2)

    def check_the_each_container(self):
        self.page_loaded(SliderSection.NEWS_BLOCK_CONTAINER)
        self.is_element_present(SliderSection.NEWS_BLOCK_CONTAINER)
        self.is_element_present(SliderSection.PHOTOS_BLOCK_CONTAINER)
        self.is_element_present(SliderSection.SCOPES_BLOCK_CONTAINER)
        self.sleep(2)

    def check_the_block_links(self):
        self.page_loaded(SliderSection.UNDER_CONTAINER_ITEMS)
        self.is_element_present(SliderSection.UNDER_CONTAINER_ITEMS)

    # Другие услуги
    def scroll_to_other_delay(self):
        self.window_scroll_by(0, 3975)
        self.sleep(2)

    def check_other_delay_container(self):
        self.page_loaded(SliderSection.CONTAINER_OTHER_DELAY)
        self.is_element_present(SliderSection.CONTAINER_OTHER_DELAY)
        self.sleep(2)

    def assert_avia_block(self):
        self.is_element_present(SliderSection.BLOCK_AVIA)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_AVIA)
        self.sleep(2)

    def assert_excursion_block(self):
        self.is_element_present(SliderSection.BLOCK_EXCURSION)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_EXCURSION)
        self.sleep(2)

    def assert_insurance_block(self):
        self.is_element_present(SliderSection.BLOCK_INSURANCE)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_INSURANCE)
        self.sleep(2)

    def assert_transfer_block(self):
        self.is_element_present(SliderSection.BLOCK_TRANSFERS)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_TRANSFERS)
        self.sleep(2)

    def assert_autobus_block(self):
        self.is_element_present(SliderSection.BLOCK_AUTOBUS)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_AUTOBUS)
        self.sleep(2)

    def assert_auto_rent(self):
        self.is_element_present(SliderSection.BLOCK_AUTO_RENT)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_AUTO_RENT)
        self.sleep(2)

    # Комментарии
    def scroll_to_comment(self):
        self.window_scroll_by(0, 4375)
        self.sleep(2)

    def check_the_comment_container(self):
        self.page_loaded(SliderSection.BLOCK_COMMENT_SECTION)
        self.is_element_present(SliderSection.BLOCK_COMMENT_SECTION)
        self.sleep(2)

    def check_the_write_comment_button(self):
        self.is_element_present(SliderSection.WRITE_COMMENT_BUTTON)
        self.assert_element_to_be_clickable(SliderSection.WRITE_COMMENT_BUTTON)
        self.sleep(2)

    def check_and_click_navigation_arrow(self):
        self.assert_element_to_be_clickable(SliderSection.BLOCK_COMMENT_NEXT)
        self.click_element(SliderSection.BLOCK_COMMENT_NEXT)
        self.sleep(2)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_COMMENT_PREV)
        self.click_element(SliderSection.BLOCK_COMMENT_PREV)
        self.sleep(2)



