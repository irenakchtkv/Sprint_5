from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
import constants


class TestLogout:

    def test_logout_successful(self, view_personal_account):

        view_personal_account.find_element(*locators.LOGOUT_BUTTON).click()

        assert WebDriverWait(view_personal_account, 3).until(expected_conditions.url_contains(constants.LOGIN_PAGE_PATH))
        assert WebDriverWait(view_personal_account, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))