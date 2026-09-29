from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
import constants


class TestConstructorSections:

    def test_bun_section_activated_by_bun_button_successful(self, driver):

        driver.get(constants.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.BURGER_ASSEMBLE_TITLE))

        driver.find_element(*locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(locators.SAUCES_SECTION, 'class', 'tab_tab_type_current__2BEPc'))
        driver.find_element(*locators.BUNS_BUTTON).click()

        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(locators.BUNS_SECTION, 'class', 'tab_tab_type_current__2BEPc'))


    def test_sauces_section_activated_by_sauces_button_successful(self, driver):

        driver.get(constants.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.BURGER_ASSEMBLE_TITLE))

        driver.find_element(*locators.SAUCES_BUTTON).click()

        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(locators.SAUCES_SECTION, 'class', 'tab_tab_type_current__2BEPc'))


    def test_fillings_section_activated_by_fillings_button_successful(self, driver):

        driver.get(constants.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.BURGER_ASSEMBLE_TITLE))

        driver.find_element(*locators.FILLINGS_BUTTON).click()

        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(locators.FILLINGS_SECTION, 'class', 'tab_tab_type_current__2BEPc'))