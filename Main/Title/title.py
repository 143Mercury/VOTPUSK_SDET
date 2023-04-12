from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from VOTPUSK.BaseMethods.object_methods import BaseMethods


class TitleLocator(BaseMethods):
    BANNER_TITLE = (By.CSS_SELECTOR, '[class="banner__image __image_pc"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def title_is_exist(self):
        self.page_loaded(TitleLocator.BANNER_TITLE)
        self.is_element_present(TitleLocator.BANNER_TITLE)





