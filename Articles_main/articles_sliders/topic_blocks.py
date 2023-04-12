import time

from VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class TopicBlocks(BaseMethods):
    TOPIC_BLOCKS_LOCATOR = (By.CSS_SELECTOR, '[class="topic__block"]')
    TOPIC_BTN = (By.CSS_SELECTOR, '[class="topic__btn"]')
    FOOTER_MENU = (By.CSS_SELECTOR, '[class="footer-menu topic-menu"]')
    DELAY = (By.XPATH, '//*[@id="all__topics"]/div/div/div/ul/li[4]')
    BY_TRAVELING_TIME = (By.XPATH, '//*[@id="all__topics"]/div/div/div/ul/li[3]')
    BY_TYPE_OF_VACATION = (By.XPATH, '//*[@id="all__topics"]/div/div/div/ul/li[2]')
    ATTRACTIONS = (By.XPATH, '//*[@id="all__topics"]/div/div/div/ul/li[1]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_all_topics_section(self):
        self.window_scroll_by(0, 2950)
        self.sleep(2)

    def check_the_topics_container(self):
        self.is_element_present(TopicBlocks.TOPIC_BLOCKS_LOCATOR)
        self.sleep(2)

    def click_to_open_more_button(self):
        self.click_element(TopicBlocks.TOPIC_BTN)
        self.sleep(2)

    def check_the_footer_menu(self):
        self.is_element_present(TopicBlocks.FOOTER_MENU)
        self.sleep(2)

    def check_each_block_offer(self):
        self.is_element_present(TopicBlocks.DELAY)
        self.is_element_present(TopicBlocks.BY_TRAVELING_TIME)
        self.is_element_present(TopicBlocks.BY_TYPE_OF_VACATION)
        self.is_element_present(TopicBlocks.ATTRACTIONS)




