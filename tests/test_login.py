from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
from generator import email_generation
from generator import valid_password_generator


def register_new_user(driver):

    driver.get('https://stellarburgers.education-services.ru')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))
    
    driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*locators.REGISTER_LINK).click()
    
    driver.find_element(*locators.NAME_INPUT_REG).send_keys('Крот')
    email = email_generation('zhu', 'li')
    driver.find_element(*locators.EMAIL_INPUT_REG).send_keys(email)
    password = valid_password_generator()
    driver.find_element(*locators.PASSWORD_INPUT_REG).send_keys(password)
    driver.find_element(*locators.REGISTER_BUTTON).click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))

    return email, password


def test_sign_in_with_login_to_account_button_successful(driver):

    email, password = register_new_user(driver)

    driver.get('https://stellarburgers.education-services.ru')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))

    driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(password)
    driver.find_element(*locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))

    assert driver.find_element(*locators.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'

    driver.quit()


def test_sign_in_with_personal_account_button_successful(driver):

    email, password = register_new_user(driver)
    
    driver.get('https://stellarburgers.education-services.ru')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PERSONAL_ACCOUNT_BUTTON))

    driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(password)
    driver.find_element(*locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))

    assert driver.find_element(*locators.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'
    
    driver.quit()


def test_sign_in_with_login_button_in_registration_form_successful(driver):

    email, password = register_new_user(driver)

    driver.get('https://stellarburgers.education-services.ru')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))

    driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*locators.REGISTER_LINK).click()
    driver.find_element(*locators.LOGIN_LINK_REG).click()

    driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(password)
    driver.find_element(*locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))
    
    assert driver.find_element(*locators.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'
    
    driver.quit()


def test_sign_in_with_login_button_in_recovery_form_successful(driver):

    email, password = register_new_user(driver)

    driver.get('https://stellarburgers.education-services.ru')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))

    driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*locators.RECOVER_PASSWORD_LINK).click()
    driver.find_element(*locators.LOGIN_LINK_RECOVERY).click()

    driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(password)
    driver.find_element(*locators.LOGIN_BUTTON).click()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))
        
    assert driver.find_element(*locators.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'

    driver.quit()