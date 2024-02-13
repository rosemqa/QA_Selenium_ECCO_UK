import allure
from .base_page import BasePage
from locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    # GETTERS
    def get_first_name_alert_text(self):
        return self.find_element(RegistrationPageLocators.FIRST_NAME_ERROR).text

    def get_last_name_alert_text(self):
        return self.find_element(RegistrationPageLocators.LAST_NAME_ERROR).text

    def get_email_alert_text(self):
        return self.find_element(RegistrationPageLocators.EMAIL_ERROR).text

    def get_password_alert_text(self):
        return self.find_element(RegistrationPageLocators.PASSWORD_ERROR).text

    def get_confirm_password_alert_text(self):
        return self.find_element(RegistrationPageLocators.CONFIRM_PASSWORD_ERROR).text

    def get_accept_terms_alert_text(self):
        return self.find_element(RegistrationPageLocators.ACCEPT_TERMS_ERROR).text

    # ACTIONS
    @allure.step('Enter First name')
    def enter_first_name(self, first_name):
        self.find_element(RegistrationPageLocators.FIRST_NAME_FIELD).send_keys(first_name)
        print('Enter First name')

    @allure.step('Enter Last name')
    def enter_last_name(self, last_name):
        self.find_element(RegistrationPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        print('Enter Last name')

    @allure.step('Enter Email')
    def enter_email(self, email):
        self.find_element(RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        print('Enter Email')

    @allure.step('Enter Password')
    def enter_password(self, password):
        self.find_element(RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        print('Enter Password')

    @allure.step('Confirm Password')
    def confirm_password(self, password):
        self.find_element(RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        print('Confirm Password')

    @allure.step('Tick the "Accept terms" checkbox')
    def accept_terms(self):
        self.find_element(RegistrationPageLocators.ACCEPT_TERMS).click()
        print('Accept terms')

    @allure.step('Click "here" link in the "Accept terms" section')
    def click_terms_link(self):
        self.find_element(RegistrationPageLocators.ACCEPT_TERMS_LINK).click()
        print('Click terms link')

    @allure.step('Click the Man radiobutton')
    def select_male_gender(self):
        self.find_element(RegistrationPageLocators.GENDER_MALE).click()
        print('Select Male gender')

    @allure.step('Click the Women radiobutton')
    def select_female_gender(self):
        self.find_element(RegistrationPageLocators.GENDER_FEMALE).click()
        print('Select the Female gender')

    @allure.step('Click the "Create account now" button')
    def click_create_account_button(self):
        self.find_element(RegistrationPageLocators.CREATE_ACCOUNT_BTN).click()
        print('Click the "Create account now" button')

    # ASSERTIONS
    @allure.step('Assert the terms window is present')
    def assert_terms_window_is_present(self):
        assert self.is_element_present(RegistrationPageLocators.TERMS_WINDOW_ELEMENT), \
            'Terms window is missing'
        print('Terms window is present')
