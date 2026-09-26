from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
from generator import email_generation
from generator import valid_password_generator


def test_logout_successful(driver):
    
    driver.get('https://stellarburgers.education-services.ru')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))
        
    driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*locators.REGISTER_LINK).click()
        
    driver.find_element(*locators.NAME_INPUT_REG).send_keys('Константин')
    email = email_generation('const', 'antin')
    driver.find_element(*locators.EMAIL_INPUT_REG).send_keys(email)
    password = valid_password_generator()
    driver.find_element(*locators.PASSWORD_INPUT_REG).send_keys(password)
    driver.find_element(*locators.REGISTER_BUTTON).click()       
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

    driver.get('https://stellarburgers.education-services.ru')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))
    
    driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(password)
    driver.find_element(*locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))

    driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PROFILE_SECTION))

    driver.find_element(*locators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

    assert '/login' in driver.current_url
    assert driver.find_element(*locators.LOGIN_TITLE).text == 'Вход'

    driver.quit()