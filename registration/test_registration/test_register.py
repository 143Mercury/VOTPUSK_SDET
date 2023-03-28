from VOTPUSK.registration.locators.registration_locators import FormLocators
from VOTPUSK.registration.TestData.Data import TestData
from VOTPUSK.registration.test_registration.conftest import login_alert


class TestRegister:
    def test_sign_in(self, driver):
        driver.get(TestData.URL)
        log_into_alert = FormLocators(driver)
        log_into_alert.log_into_alert()
        totally_register = FormLocators(driver)
        totally_register.totally_register()
        check_existing_eye = FormLocators(driver)
        check_existing_eye.check_existing_eye()
        check_the_agreement_button = FormLocators(driver)
        check_the_agreement_button.check_the_agreement_button()
        create_account = FormLocators(driver)
        create_account.create_account()
