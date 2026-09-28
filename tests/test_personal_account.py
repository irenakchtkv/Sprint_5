from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
import constants


class TestPersonalAccount:

    def test_personal_account_transition_to_profile_section_successful(self, authorize_user):
        
        authorize_user.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()

        assert WebDriverWait(authorize_user, 3).until(expected_conditions.url_contains(constants.USER_PROFILE_PATH))
        assert WebDriverWait(authorize_user, 3).until(expected_conditions.visibility_of_element_located(locators.PROFILE_SECTION))