import allure
from selenium.webdriver import ActionChains, Keys
from locators import AccountPageLocators
from .base_page import BasePage


class AccountPage(BasePage):
    # GETTERS
    def get_greeting_title_text(self):
        return self.find_element(AccountPageLocators.GREETING_TITLE).text

    # ASSERTIONS
    def assert_greeting_title_is_present(self):
        assert self.is_element_present(AccountPageLocators.GREETING_TITLE), \
            'Greeting title is missing'
        print('Greeting title is present')
