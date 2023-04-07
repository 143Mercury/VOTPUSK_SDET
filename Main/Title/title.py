from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from VOTPUSK_SDET.VOTPUSK.BaseMethods.object_methods import BaseMethods


class TitleLocator(BaseMethods):
    BANNER_TITLE = (By.CSS_SELECTOR, '[class="banner__image __image_pc"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def title_is_exist(self):
        title = self.wait_until_element_visible(TitleLocator.BANNER_TITLE)
        return title




