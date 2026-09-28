from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
import constants


class TestConstructorNavigation:

    def test_profile_section_transition_to_constructor_by_constructor_button_successful(self, view_personal_account):

        view_personal_account.find_element(*locators.CONSTRUCTOR_BUTTON).click()

        assert view_personal_account.current_url == constants.MAIN_URL
        assert WebDriverWait(view_personal_account, 3).until(expected_conditions.visibility_of_element_located(locators.BURGER_ASSEMBLE_TITLE))

    def test_profile_section_transition_to_constructor_by_logo_successful(self, view_personal_account):

        view_personal_account.find_element(*locators.STELLAR_BURGERS_LOGO).click()
    
        assert view_personal_account.current_url == constants.MAIN_URL
        assert WebDriverWait(view_personal_account, 3).until(expected_conditions.visibility_of_element_located(locators.BURGER_ASSEMBLE_TITLE))