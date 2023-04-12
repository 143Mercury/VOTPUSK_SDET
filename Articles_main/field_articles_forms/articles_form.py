from abc import ABC

from VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class ArticlesFormLocators(BaseMethods, ABC):
    FORM_CONTAINER = (By.CSS_SELECTOR, '[class="form__block-wrapper"]')
    FORM_LIST_CONTAINER_COUNTRY = (By.CSS_SELECTOR, '[id="select2-countries_list-container"]')
    FORM_LIST_CONTAINER_CITIES = (By.CSS_SELECTOR, '[id="select2-cities_list-container"]')
    FORM_LIST_CONTAINER_THEMES = (By.CSS_SELECTOR, '[id="select2-subjects_list-container"]')
    LIST_CONTAINER_COUNTRY_CITIES_THEMES = (By.CSS_SELECTOR, '[class="select2-results"]')

    SEARCH_ARTICLES_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_locator(self):
        self.window_scroll_by(0, 450)
        self.sleep(2)

    def assert_container_country(self):
        self.is_element_present(ArticlesFormLocators.FORM_LIST_CONTAINER_COUNTRY)
        self.sleep(2)

    def select_random_randint_country(self):
        self.click_element(ArticlesFormLocators.FORM_LIST_CONTAINER_COUNTRY)
        self.random_country_selection(ArticlesFormLocators.FORM_LIST_CONTAINER_COUNTRY)
        self.sleep(2)

    def assert_container_cities(self):
        self.is_element_present(ArticlesFormLocators.FORM_LIST_CONTAINER_CITIES)
        self.sleep(2)

    def select_random_randint_cities(self):
        self.click_element(ArticlesFormLocators.FORM_LIST_CONTAINER_CITIES)
        self.random_country_selection(ArticlesFormLocators.LIST_CONTAINER_COUNTRY_CITIES_THEMES)
        self.sleep(2)

    def assert_container_themes(self):
        self.is_element_present(ArticlesFormLocators.FORM_LIST_CONTAINER_THEMES)
        self.sleep(2)

    def select_random_randint_themes(self):
        self.click_element(ArticlesFormLocators.FORM_LIST_CONTAINER_THEMES)
        self.random_country_selection(ArticlesFormLocators.LIST_CONTAINER_COUNTRY_CITIES_THEMES)
        self.sleep(2)
