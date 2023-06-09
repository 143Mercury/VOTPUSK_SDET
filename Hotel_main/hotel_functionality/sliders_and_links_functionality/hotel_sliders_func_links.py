import time

from VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


#  Проверка заголовка
class SlidersHotelLinksLocator(BaseMethods):
    H3_POPULAR_DESIGN = (By.CSS_SELECTOR, '[class="container hotels-h3 blue-hotels"]')
    SLIDER_HOTEL_CONTAINER = (By.CSS_SELECTOR, '[class="swiper swiper-hotels-dir corner-radius-two-50 '
                                               'swiper-initialized swiper-horizontal swiper-pointer-events"]')
    SLIDER_NAVIGATION_ARROW_NEXT = (By.XPATH, '//*[@id="page-header"]/section[2]/div[2]/div/button[2]')
    SLIDER_NAVIGATION_ARROW_PREV = (By.XPATH, '//*[@id="page-header"]/section[2]/div[2]/div/button[1]')
    # Проверка контейнера популярных направлений Отелей
    HOTEL_CONTAINER_BLOCK = (By.CSS_SELECTOR, '[class="hotels-popular-dir__grid"]')
    HOTEL_POPULAR_BLOCK_1 = (By.XPATH, '//*[@id="page-header"]/section[2]/div[3]/div[1]')
    HOTEL_POPULAR_BLOCK_2 = (By.XPATH, '//*[@id="page-header"]/section[2]/div[3]/div[2]')
    HOTEL_POPULAR_BLOCK_3 = (By.XPATH, '//*[@id="page-header"]/section[2]/div[3]/div[3]')
    HOTEL_POPULAR_BLOCK_4 = (By.XPATH, '//*[@id="page-header"]/section[2]/div[3]/div[4]')
    HOTEL_POPULAR_BLOCK_5 = (By.XPATH, '//*[@id="page-header"]/section[2]/div[3]/div[5]')
    HOTEL_POPULAR_BLOCK_6 = (By.XPATH, '//*[@id="page-header"]/section[2]/div[3]/div[6]')
    HOTEL_POPULAR_BLOCK_7 = (By.XPATH, '//*[@id="page-header"]/section[2]/div[3]/div[7]')
    HOTEL_POPULAR_BLOCK_8 = (By.XPATH, '//*[@id="page-header"]/section[2]/div[3]/div[8]')
    LINK_UNDER_LINE = (By.CSS_SELECTOR, '[class="link-underline"]')
    # Проверка под-заголовка + проверка лидеров предложений
    HOTELS_H2 = (By.CSS_SELECTOR, '[class="hotels-h2"]')
    HOTEL_LEADERS_OFFER = (By.CSS_SELECTOR, '[class="hotels-leaders"]')
    AGADA_OFFER = (By.CSS_SELECTOR, '[alt="Agoda"]')
    HOTELS_COM_OFFER = (By.CSS_SELECTOR, '[alt="Hotels.com"]')
    SNAP_TRAVEL_OFFER = (By.CSS_SELECTOR, '[alt="Snaptravel"]')
    OSTROVOK_RU_OFFER = (By.CSS_SELECTOR, '[alt="Ostrovok"]')
    TRIP_COM_OFFER = (By.CSS_SELECTOR, '[alt="Trip.com"]')
    HOSTEL_WORLD_OFFER = (By.CSS_SELECTOR, '[alt="Hostelworld"]')
    SUTOCHNO_RU_OFFER = (By.CSS_SELECTOR, '[alt="SutochnoRu"]')
    TVIL_RU_OFFER = (By.CSS_SELECTOR, '[alt="TvilRu"]')

    # Проверка блока комментарии
    HOTEL_COMMENT_SECTION_CONTAINER = (By.XPATH, '//*[@id="page-header"]/div[1]/div[4]/div')
    # HOTEL_COMMENT_DATA = (By.CSS_SELECTOR, '[class="swiper-slide swiper-slide-duplicate swiper-slide-active"]]')
    # HOTEL_COMMENT_DATA_HEADER = (By.XPATH, '//*[@id="swiper-wrapper-ad521bfa5ed4c1d3"]/div[3]/header')
    # HOTEL_COMMENT_DATA_STAR = (By.XPATH, '//*[@id="swiper-wrapper-ad521bfa5ed4c1d3"]/div[3]/header/div')
    HOTEL_COMMENT_SECTION_NAVIGATION_ARROW_NEXT = (By.XPATH, '//*[@id="page-header"]/div[1]/div[4]/button[2]')
    HOTEL_COMMENT_SECTION_NAVIGATION_ARROW_PREV = (By.XPATH, '//*[@id="page-header"]/div[1]/div[4]/button[1]')
    LINK_COMMENT_UNDER_LINE = (By.CSS_SELECTOR, '[class="orange-underline"]')
    LEAVE_COMMENT_BUTTON = (By.CSS_SELECTOR, '[class="btn-orange"]')

    # Проверка блока Вопросы/Ответы
    H3_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[1]')
    FULL_BLOCK_1 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[1]')
    UNDER_BLOCK_INFO_1 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[1]/small')
    FULL_BLOCK_2 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[2]')
    UNDER_BLOCK_INFO_2 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[2]/small')
    FULL_BLOCK_3 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[3]')
    UNDER_BLOCK_INFO_3 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[3]/small')
    FULL_BLOCK_4 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[4]')
    UNDER_BLOCK_INFO_4 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[4]/small')
    FULL_BLOCK_5 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[5]')
    UNDER_BLOCK_INFO_5 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[5]/small')
    FULL_BLOCK_6 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[6]')
    UNDER_BLOCK_INFO_6 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[6]/small')
    FULL_BLOCK_7 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[7]')
    UNDER_BLOCK_INFO_7 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[7]/small')
    FULL_BLOCK_8 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[8]')
    UNDER_BLOCK_INFO_8 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div[2]/div[8]/small')

    LINK_UNDER_FAQ = (By.CSS_SELECTOR, '[class="link-underline hotels-faq__all"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_popular_sections(self):  # Scroll до нужного элемента
        self.window_scroll_by(0, 450)

    def check_the_text_h3(self):  #
        self.is_visible(SlidersHotelLinksLocator.H3_POPULAR_DESIGN)  # Проверка h3

    def check_all_container_blocks(self):  #
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_CONTAINER_BLOCK)

    def check_all_same_hotel_locators(self):  #
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_POPULAR_BLOCK_1)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_POPULAR_BLOCK_2)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_POPULAR_BLOCK_3)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_POPULAR_BLOCK_4)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_POPULAR_BLOCK_5)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_POPULAR_BLOCK_6)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_POPULAR_BLOCK_7)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_POPULAR_BLOCK_8)

    def check_link_under_line(self):  #
        self.is_element_present(SlidersHotelLinksLocator.LINK_UNDER_LINE)

    def scroll_into_view_hotels_offer(self):  #
        self.window_scroll_by(0, 950)

    def check_the_h2(self):
        self.is_visible(SlidersHotelLinksLocator.HOTELS_H2)

    def check_the_hotels_leaders_offer(self):
        time.sleep(2)
        self.is_element_present(SlidersHotelLinksLocator.AGADA_OFFER)
        self.is_element_present(SlidersHotelLinksLocator.HOTELS_COM_OFFER)
        self.is_element_present(SlidersHotelLinksLocator.SNAP_TRAVEL_OFFER)
        self.is_element_present(SlidersHotelLinksLocator.OSTROVOK_RU_OFFER)
        self.is_element_present(SlidersHotelLinksLocator.TRIP_COM_OFFER)
        self.is_element_present(SlidersHotelLinksLocator.HOSTEL_WORLD_OFFER)
        self.is_element_present(SlidersHotelLinksLocator.SUTOCHNO_RU_OFFER)
        self.is_element_present(SlidersHotelLinksLocator.TVIL_RU_OFFER)

    def hotel_scroll_into_comment_section(self):
        self.window_scroll_by(0, 1350)

    def check_the_comment_blocks(self):
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_COMMENT_SECTION_CONTAINER)

    """def check_comment_data(self):
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_COMMENT_DATA)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_COMMENT_DATA_HEADER)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_COMMENT_DATA_STAR)"""

    def assert_navigation_arrows_clickable(self):
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_COMMENT_SECTION_NAVIGATION_ARROW_NEXT)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.HOTEL_COMMENT_SECTION_NAVIGATION_ARROW_NEXT)
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_COMMENT_SECTION_NAVIGATION_ARROW_PREV)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.HOTEL_COMMENT_SECTION_NAVIGATION_ARROW_PREV)

    def scroll_to_FAQ(self):
        self.window_scroll_by(0, 1900)

    def check_response_container(self):
        self.is_element_present(SlidersHotelLinksLocator.H3_BLOCK)

    def check_adjust_blocks(self):
        self.is_element_present(SlidersHotelLinksLocator.FULL_BLOCK_1)
        self.is_visible(SlidersHotelLinksLocator.UNDER_BLOCK_INFO_1)
        time.sleep(1)
        self.is_element_present(SlidersHotelLinksLocator.FULL_BLOCK_2)
        self.is_visible(SlidersHotelLinksLocator.UNDER_BLOCK_INFO_2)
        time.sleep(1)
        self.is_element_present(SlidersHotelLinksLocator.FULL_BLOCK_3)
        self.is_visible(SlidersHotelLinksLocator.UNDER_BLOCK_INFO_3)
        time.sleep(1)
        self.is_element_present(SlidersHotelLinksLocator.FULL_BLOCK_4)
        self.is_visible(SlidersHotelLinksLocator.UNDER_BLOCK_INFO_4)
        time.sleep(1)
        self.is_element_present(SlidersHotelLinksLocator.FULL_BLOCK_5)
        self.is_visible(SlidersHotelLinksLocator.UNDER_BLOCK_INFO_5)
        time.sleep(1)
        self.is_element_present(SlidersHotelLinksLocator.FULL_BLOCK_6)
        self.is_visible(SlidersHotelLinksLocator.UNDER_BLOCK_INFO_6)
        time.sleep(1)
        self.is_element_present(SlidersHotelLinksLocator.FULL_BLOCK_7)
        self.is_visible(SlidersHotelLinksLocator.UNDER_BLOCK_INFO_7)
        time.sleep(1)
        self.is_element_present(SlidersHotelLinksLocator.FULL_BLOCK_8)
        self.is_visible(SlidersHotelLinksLocator.UNDER_BLOCK_INFO_8)

    def checking_clickable_faq(self):
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.FULL_BLOCK_1)
        time.sleep(1)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.FULL_BLOCK_2)
        time.sleep(1)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.FULL_BLOCK_3)
        time.sleep(1)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.FULL_BLOCK_4)
        time.sleep(1)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.FULL_BLOCK_5)
        time.sleep(1)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.FULL_BLOCK_6)
        time.sleep(1)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.FULL_BLOCK_7)
        time.sleep(1)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.FULL_BLOCK_8)
        time.sleep(1)

    def check_hotel_faq_link_under_line(self):
        self.is_element_present(SlidersHotelLinksLocator.LINK_UNDER_FAQ)
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.LINK_UNDER_FAQ)




