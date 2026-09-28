from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
import constants


class TestLogin:

    def test_sign_in_with_login_to_account_button_successful(self, register_new_user):

        driver, email, password = register_new_user

        driver.get(constants.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))

        driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(password)
        driver.find_element(*locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 3).until(expected_conditions.url_to_be(constants.MAIN_URL))
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))


    def test_sign_in_with_personal_account_button_successful(self, register_new_user):

        driver, email, password = register_new_user
    
        driver.get(constants.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PERSONAL_ACCOUNT_BUTTON))

        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(password)
        driver.find_element(*locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 3).until(expected_conditions.url_to_be(constants.MAIN_URL))
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))


    def test_sign_in_with_login_button_in_registration_form_successful(self, register_new_user):

        driver, email, password = register_new_user

        driver.get(constants.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))

        driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.REGISTER_LINK).click()
        driver.find_element(*locators.LOGIN_LINK_REG).click()

        driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(password)
        driver.find_element(*locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 3).until(expected_conditions.url_to_be(constants.MAIN_URL))
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))


    def test_sign_in_with_login_button_in_recovery_form_successful(self, register_new_user):

        driver, email, password = register_new_user

        driver.get(constants.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))

        driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.RECOVER_PASSWORD_LINK).click()
        driver.find_element(*locators.LOGIN_LINK_RECOVERY).click()

        driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(password)
        driver.find_element(*locators.LOGIN_BUTTON).click()
            
        assert WebDriverWait(driver, 3).until(expected_conditions.url_to_be(constants.MAIN_URL))
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))