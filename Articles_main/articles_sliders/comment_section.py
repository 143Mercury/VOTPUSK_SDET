import time

from selenium.webdriver.common.by import By
from VOTPUSK.BaseMethods.object_methods import BaseMethods


class CommentLocator(BaseMethods):
    COMMENT_CONTAINER = (By.XPATH, '//*[@id="page-header"]/section[9]/div')
    COMMENT_TEXT = (By.XPATH, '//*[@id="page-header"]/section[9]/div/div/div[1]/a[1]/div[2]/div/p')
    SHOW_MORE_LINK = (By.CSS_SELECTOR, '[class="more-comments__item more-comments__item-enabled active"]')
    LIKE_OPTIONS = (By.XPATH, '//*[@id="page-header"]/section[9]/div/div/div[1]/a[1]/div[1]/div[2]/div[2]')
    AD = (By.CSS_SELECTOR, '[class="top-block top-block-desktop"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_into_view(self):
        self.window_scroll_by(0, 4250)
        self.sleep(2)

    def assert_visibility_of_container(self):
        self.is_element_present(CommentLocator.COMMENT_CONTAINER)
        self.sleep(2)

    def assert_text_area(self):
        self.is_element_present(CommentLocator.COMMENT_TEXT)
        self.sleep(2)

    def assert_like_area(self):
        self.is_element_present(CommentLocator.LIKE_OPTIONS)
        self.sleep(2)

    def assert_how_more_options(self):
        self.is_element_present(CommentLocator.SHOW_MORE_LINK)
        self.sleep(2)

    def assert_element_clickable(self):
        self.assert_element_to_be_clickable(CommentLocator.SHOW_MORE_LINK)
        self.sleep(2)

    def assert_ad_block(self):
        self.is_element_present(CommentLocator.AD)


