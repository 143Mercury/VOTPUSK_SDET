import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


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
    ARTICLES_BLOCKS_CONTAINER = (By.CSS_SELECTOR, '[class="articles__slider swiper swiper-initialized '
                                                  'swiper-horizontal swiper-pointer-events"]')

    ARTICLES_SLIDERS_NEXT = (By.CSS_SELECTOR, 'class="swiper-button-next articles__slider_next"')
    ARTICLES_SLIDERS_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev articles__slider_prev"]')
    CHECK_ALL_ARTICLES_ITEM = (By.XPATH, '/html/body/section[6]/div/div/div/div[3]/a')
    # Форма поиска статей
    FIELD_FORM_BLOCK = (By.CSS_SELECTOR, '[class="articles__search"]')

    OPEN_CONTAINER_COUNTRY = (By.CSS_SELECTOR, '[id="select2-country-container"]')
    CONTAINER_COUNTRY = (By.CSS_SELECTOR, '')
    OPEN_CONTAINER_CITIES = (By.CSS_SELECTOR, '[id="select2-city-container"]')
    CONTAINER_CITIES = (By.CSS_SELECTOR, '')
    OPEN_CONTAINER_THEMES = (By.CSS_SELECTOR, '[id="select2-theme-container"]')
    CONTAINER_THEMES = (By.CSS_SELECTOR, '')

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
    CONTAINER_TRAINS = (By.CSS_SELECTOR, '[class="container container_tickets"]')
    CONTAINER_TRAINS_SLIDER_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next tickets__slider_next"]')
    CONTAINER_TRAINS_SLIDER_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev tickets__slider_prev"]')
    CONTAINER_TRAINS_BOOKING_TICKETS_ITEM = (By.CSS_SELECTOR, '[class="tickets__order-redirect"]')
    TRAIN_BLOCKS = [
        (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[6]/picture/img'),
        (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[7]/picture/img'),
        (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[8]/picture/img'),
        (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[9]/picture/img'),
    ]

    # Новости - Фоторепортажи - Калейдоскоп
    CONTAINER_ITEM_NEWS_PHOTO = (By.XPATH, '/html/body/article/div')
    NEWS_BLOCK_CONTAINER = (By.CSS_SELECTOR, '[class="news__wrapper"]')
    PHOTOS_BLOCK_CONTAINER = (By.CSS_SELECTOR, '[class="photos__wrapper"]')
    SCOPES_BLOCK_CONTAINER = (By.CSS_SELECTOR, '[class="kaleidoscopes__wrapper"]')

    UNDER_CONTAINER_ITEMS = (By.CSS_SELECTOR, '[class="gallery__order-redirect"]')

    # Другие услуги
    CONTAINER_OTHER_DELAY = (By.CSS_SELECTOR, '[class="other-services__wrapper"]')

    # Отзывы о Votpusk.ru
    BLOCK_COMMENT_SECTION = (By.CSS_SELECTOR, '[class="reviews__slider swiper swiper-initialized swiper-horizontal '
                                              'swiper-pointer-events"]')
    WRITE_COMMENT_BUTTON = (By.CSS_SELECTOR, '[class="reviews__btn"]')
    BLOCK_COMMENT_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next reviews__slider_next"]')
    BLOCK_COMMENT_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev reviews__slider_prev"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def do_check_block_tours_option(self):
        self.assert_elements_exist(SliderSection.BLOCK_VACATION_TYPE_WRAPPER)
        self.check_container(SliderSection.BLOCK_VACATION_TYPE_WRAPPER)

    def check_tour_container(self):
        self.check_container(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        time.sleep(3)

    def check_each_blocks_to_exist_tours_first(self):
        self.is_element_present(SliderSection.FIRST_TOUR_BLOCK)
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.SECOND_TOUR_BLOCK)
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.THIRD_TOUR_BLOCK)

    def check_each_blocks_to_exist(self):
        self.click_element(SliderSection.TOURS_SLIDER_NEXT)
        time.sleep(2)

    """def check_each_blocks_to_exist_tours_second(self):
        self.is_element_present(SliderSection.FOURTH_TOUR_BLOCK)
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.FIFTH_TOUR_BLOCK)
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.SIXTH_TOUR_BLOCK)"""

    def check_tour_container_again(self):
        self.is_element_present(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        self.assert_elements_exist(SliderSection.TOURS_ALL_ITEM_CONTAINER)

    def switch_tour_section(self):
        self.assert_elements_exist(SliderSection.TOUR_SWITCHER)
        self.click_element(SliderSection.TOUR_SWITCHER)
        WebDriverWait(self.driver, 5)

    def check_the_container_inside(self):
        self.is_element_present(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        self.assert_elements_exist(SliderSection.TOURS_ALL_ITEM_CONTAINER)

    def slide_to_next_blocks(self):
        self.click_element(SliderSection.TOURS_SLIDER_WORLD_NEXT)
        time.sleep(3)
        self.is_element_present(SliderSection.TOURS_ALL_ITEM_CONTAINER)

    def check_the_tour_order_button(self):
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.CHECK_THE_ORDER_FUNCTION)

    def scroll_to_page_articles(self):
        self.scroll_page_articles()

    def check_the_block_of_articles(self):
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.ARTICLES_BLOCKS_CONTAINER)

    def scroll_and_check_the_blocks_container(self):
        self.do_randint_click(SliderSection.ARTICLES_SLIDERS_NEXT)
        self.is_element_present(SliderSection.ARTICLES_BLOCKS_CONTAINER)



