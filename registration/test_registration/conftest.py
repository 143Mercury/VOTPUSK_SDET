import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def login_alert(driver, username, password):
    wait = WebDriverWait(driver, 15)
    alert = wait.until(EC.alert_is_present())
    alert.driver.switch_to.alert()
    alert.send_keys(username)
    alert.send_keys(password)
    alert.accept()
