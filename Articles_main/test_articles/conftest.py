import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def setup_class(cls):
    cls.driver = cls.driver


def teardown_class(cls):
    cls.driver.quit()
