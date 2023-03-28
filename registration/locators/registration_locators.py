from VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By
from VOTPUSK.registration.test_registration.conftest import login_alert
from VOTPUSK.registration.TestData.Data import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormLocators(BaseMethods):
    CHECK_IN = (By.CSS_SELECTOR, '[class="header__social-icon header__social-icon_user header__social-icon_no-login"]')
    SWITCH_TO_REGISTRATION = (By.CSS_SELECTOR, '[class="switch-btn reg-btn"]')
    LOGIN_INPUT = (By.CSS_SELECTOR, '[name="RegisterForm[email]"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="registerform-pass"]')
    INVISIBLE_EYE = (By.XPATH, '//*[@id="register-form"]/div[2]/div/button/img[1]')
    CHECK_MARK = (By.CSS_SELECTOR, '[class="policy__wrapper-checkmark"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-primary register-btn"]')
    LOGIN_SWITCHER = (By.CSS_SELECTOR, '[class="switch-btn login-btn"]')
    EMAIL = (By.CSS_SELECTOR, '[id="loginform-email"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[id="loginform-pass"]')
    RESET_PASS = (By.CSS_SELECTOR, '[class="reset-popup-btn"]')
    LOG_IN = (By.CSS_SELECTOR, 'class="btn btn-primary auth-btn"')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def log_into_alert(self):
        self.click_element(FormLocators.CHECK_IN)
        self.sleep(3)
        self.click_element(FormLocators.SWITCH_TO_REGISTRATION)

    def totally_register(self):
        self.sleep(4)
        self.send_keys_to_element(FormLocators.LOGIN_INPUT, TestData.LOG_IN_INPUT)
        self.send_keys_to_element(FormLocators.PASSWORD_INPUT, TestData.PASSWORD_INPUT)

    def check_existing_eye(self):
        self.sleep(3)
        self.is_element_present(FormLocators.INVISIBLE_EYE)

    def check_the_agreement_button(self):
        self.sleep(3)
        self.is_element_present(FormLocators.CHECK_MARK)

    def create_account(self):
        self.click_element(FormLocators.REGISTER_BUTTON)