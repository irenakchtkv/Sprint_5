import pytest
import locators
import constants
import generator
from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

@pytest.fixture
def authorize_user(driver):

    driver.get(constants.MAIN_URL)

    driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*locators.EMAIL_INPUT_AUTH).send_keys(constants.TEST_USER_EMAIL)
    driver.find_element(*locators.PASSWORD_INPUT_AUTH).send_keys(constants.TEST_USER_PASSWORD)
    driver.find_element(*locators.LOGIN_BUTTON).click()
        
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PLACE_AN_ORDER_BUTTON))

    return driver

@pytest.fixture
def view_personal_account(authorize_user):

    authorize_user.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(authorize_user, 3).until(expected_conditions.url_contains(constants.USER_PROFILE_PATH))

    return authorize_user

@pytest.fixture
def register_new_user(driver):

    driver.get(constants.MAIN_URL)

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TO_ACCOUNT_BUTTON))
        
    driver.find_element(*locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*locators.REGISTER_LINK).click()
        
    driver.find_element(*locators.NAME_INPUT_REG).send_keys('Крот')
    email = generator.email_generation('zhu', 'li')
    driver.find_element(*locators.EMAIL_INPUT_REG).send_keys(email)
    password = generator.valid_password_generator()
    driver.find_element(*locators.PASSWORD_INPUT_REG).send_keys(password)
    driver.find_element(*locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_contains(constants.LOGIN_PAGE_PATH))

    return driver, email, password