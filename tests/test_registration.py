from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
import constants
from generator import email_generation
from generator import valid_password_generator
from generator import invalid_password_generator


class TestRegistration:

    def test_registration_with_valid_email_and_password_successful(self, driver):
        
        driver.get(constants.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))

        driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.REGISTER_LINK).click()

        driver.find_element(*locators.NAME_INPUT_REG).send_keys('Гуля')
        driver.find_element(*locators.EMAIL_INPUT_REG).send_keys(email_generation('kotya', 'pipka'))
        driver.find_element(*locators.PASSWORD_INPUT_REG).send_keys(valid_password_generator())
        driver.find_element(*locators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 3).until(expected_conditions.url_contains(constants.LOGIN_PAGE_PATH))
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))


    def test_registration_with_invalid_password_shows_error_message(self, driver):

        driver.get(constants.MAIN_URL)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))
        
        driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.REGISTER_LINK).click()
        
        driver.find_element(*locators.NAME_INPUT_REG).send_keys('Маша')
        driver.find_element(*locators.EMAIL_INPUT_REG).send_keys(email_generation('missi', 'kissi'))
        driver.find_element(*locators.PASSWORD_INPUT_REG).send_keys(invalid_password_generator())
        driver.find_element(*locators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.ERROR_MESSAGE))

