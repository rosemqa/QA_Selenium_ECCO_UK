import allure
from selenium.webdriver import ActionChains, Keys
from locators import AccountPageLocators
from .base_page import BasePage


class AccountPage(BasePage):
    # GETTERS
    def get_greeting_title_text(self):
        return self.find_element(AccountPageLocators.GREETING_TITLE).text
