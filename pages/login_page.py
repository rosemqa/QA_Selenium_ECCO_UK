import allure
from .base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):

    # GETTERS
    def get_email_alert_text(self):
        return self.find_element(LoginPageLocators.EMAIL_ERROR).text

    def get_password_alert_text(self):
        return self.find_element(LoginPageLocators.PASSWORD_ERROR).text

    def get_login_failed_alert_text(self):
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text

    # ACTIONS
    @allure.step('Enter Email')
    def enter_email(self, email):
        self.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(email)
        print('Enter Email')

    @allure.step('Enter password')
    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        print('Enter password')

    @allure.step('Click "show password" button')
    def click_show_password_button(self):
        self.find_element(LoginPageLocators.SHOW_PASSWORD_BTN).click()
        print('Click "show password" button')

    @allure.step('Click "hide password" button')
    def click_hide_password_button(self):
        self.find_element(LoginPageLocators.HIDE_PASSWORD_BTN).click()
        print('Click "hide password" button')

    @allure.step('Click "Sign in now" button')
    def click_sign_in_button(self):
        self.find_element(LoginPageLocators.SIGN_IN_BTN).click()
        print('Click "Sign in now" button')

    @allure.step('Click "Forgot password" link')
    def click_forgot_password_link(self):
        self.find_element(LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        print('Click "Forgot password" link')

    @allure.step('Click "Create account" button')
    def click_create_account_button(self):
        self.find_element(LoginPageLocators.CREATE_ACCOUNT_BTN).click()
        print('Click "Create account" button')

    # ASSERTIONS
    @allure.step('Assert "Show password" button changed to "Hide password" button')
    def assert_show_password_button_changed_to_hide(self):
        assert self.is_element_present(LoginPageLocators.HIDE_PASSWORD_BTN), \
            'Show password button is not changed to Hide'
        print('Show password button changed to Hide password button')

    @allure.step('Assert password is not masked (password shown)')
    def assert_password_is_not_masked(self):
        assert self.find_element(LoginPageLocators.PASSWORD_FIELD).get_attribute('type') == "text", \
            'Password is masked'
        print('Password is shown')

    @allure.step('Assert "Hide password" button changed to "Show password" button')
    def assert_hide_password_button_changed_to_show(self):
        assert self.is_element_present(LoginPageLocators.SHOW_PASSWORD_BTN), \
            'Hide password button is not changed to Show'
        print('Hide password button changed to Show password button')

    @allure.step('Assert password is masked (password hidden)')
    def assert_password_is_masked(self):
        assert self.find_element(LoginPageLocators.PASSWORD_FIELD).get_attribute('type') == "password", \
            'Password is not masked'
        print('Password is hidden')

    @allure.step('Assert the "Sign in now" button is present')
    def assert_sign_in_btn_is_present(self):
        assert self.is_element_present(LoginPageLocators.SIGN_IN_BTN), \
            'Sign in button is missing'
        print('Sign in button is present')
