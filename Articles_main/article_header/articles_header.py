import time

from VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ArticleHeaderLocator(BaseMethods):
    HEADER_LOCATOR = (By.CSS_SELECTOR, '[alt="promo"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_the_article_header_exist(self):
        self.page_loaded(ArticleHeaderLocator.HEADER_LOCATOR)
        self.is_element_present(ArticleHeaderLocator.HEADER_LOCATOR)
