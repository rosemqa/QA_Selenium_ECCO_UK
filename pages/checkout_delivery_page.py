import allure
from faker import Faker
from .base_page import BasePage
from locators import CheckoutDeliveryPageLocators


class CheckoutDeliveryPage(BasePage):
    # GETTERS
    def get_billing_street_error_text(self):
        return self.find_element(CheckoutDeliveryPageLocators.BILLING_STREET_ERROR).text

    def get_billing_number_error_text(self):
        return self.find_element(CheckoutDeliveryPageLocators.BILLING_NUMBER_ERROR).text

    def get_billing_post_code_error_text(self):
        return self.find_element(CheckoutDeliveryPageLocators.BILLING_POST_CODE_ERROR).text

    def get_billing_city_error_text(self):
        return self.find_element(CheckoutDeliveryPageLocators.BILLING_CITY_ERROR).text

    def get_accept_consent_error(self):
        return self.find_element(CheckoutDeliveryPageLocators.ACCEPT_CONSENT_ERROR).text

    def get_css_accept_terms_checkbox_color_value(self):
        """Get css value for the border color of accept terms checkbox"""
        return self.find_element(CheckoutDeliveryPageLocators.ACCEPT_TERMS_CHECKBOX)\
            .value_of_css_property('border-color')

    def get_consent_modal_title_text(self):
        """Get the title text in the terms modal"""
        return self.find_element(CheckoutDeliveryPageLocators.CONSENT_MODAL_TITLE).text

    # ACTIONS
    @allure.step('Enter the billing address street')
    def enter_billing_address_street(self, street):
        self.find_element(CheckoutDeliveryPageLocators.BILLING_ADDRESS_STREET_FIELD).send_keys(street)
        print('Enter the billing address street')

    @allure.step('Enter the billing address building number')
    def enter_billing_address_number(self, building_number):
        self.find_element(CheckoutDeliveryPageLocators.BILLING_ADDRESS_NUMBER_FIELD).send_keys(building_number)
        print('Enter the billing address building number')

    @allure.step('Enter the billing address city')
    def enter_billing_address_city(self, city):
        self.find_element(CheckoutDeliveryPageLocators.BILLING_ADDRESS_CITY_FIELD).send_keys(city)
        print('Enter the billing address city')

    @allure.step('Enter the phone number')
    def enter_phone_number(self, phone_number):
        self.find_element(CheckoutDeliveryPageLocators.PHONE_NUMBER_FIELD).send_keys(phone_number)
        print('Enter the phone number')

    @allure.step('Enter the billing address post code')
    def enter_billing_address_post_code(self, post_code):
        self.find_element(CheckoutDeliveryPageLocators.BILLING_ADDRESS_POST_CODE_FIELD).send_keys(post_code)
        print('Enter the billing address post code')

    @allure.step('Select the accept terms checkbox')
    def select_accept_terms_checkbox(self):
        self.find_element(CheckoutDeliveryPageLocators.ACCEPT_TERMS_CHECKBOX).click()
        print('Select the accept terms checkbox')

    @allure.step('Click Go To Summary button')
    def click_go_to_summary_button(self):
        self.find_element(CheckoutDeliveryPageLocators.GO_TO_SUMMARY_BTN).click()
        print('Click Go To Summary button')

    @allure.step('Clear the billing address street field')
    def clear_billing_address_street(self):
        self.find_element(CheckoutDeliveryPageLocators.BILLING_ADDRESS_STREET_FIELD).clear()
        print('Clear the billing address street field')

    @allure.step('Clear the billing address number field')
    def clear_billing_address_number(self):
        self.find_element(CheckoutDeliveryPageLocators.BILLING_ADDRESS_NUMBER_FIELD).clear()
        print('Clear the billing address number field')

    @allure.step('Clear the billing address post code field')
    def clear_billing_address_post_code(self):
        self.find_element(CheckoutDeliveryPageLocators.BILLING_ADDRESS_POST_CODE_FIELD).clear()
        print('Clear the billing address post code field')

    @allure.step('Clear the billing address city field')
    def clear_billing_address_city(self):
        self.find_element(CheckoutDeliveryPageLocators.BILLING_ADDRESS_CITY_FIELD).clear()
        print('Clear the billing address city field')

    @allure.step('Click Terms and Conditions link')
    def click_terms_and_conditions_link(self):
        self.find_element(CheckoutDeliveryPageLocators.TERMS_AND_CONDITIONS_LINK).click()
        print('Click Terms and Conditions link')

    @allure.step('Click Accept Privacy Policy link')
    def click_accept_privacy_policy_link(self):
        self.find_element(CheckoutDeliveryPageLocators.ACCEPT_PRIVACY_POLICY_LINK).click()
        print('Click Accept Privacy Policy link')

    @allure.step('Click Close icon in the Terms and Conditions or Accept Privacy Policy modal')
    def click_close_consent_modal_icon(self):
        self.find_element(CheckoutDeliveryPageLocators.CLOSE_CONSENT_MODAL_ICON).click()
        print('Click Close icon in the Terms and Conditions or Accept Privacy Policy modal')

    # METHODS
    @allure.step('Enter the billing address on the checkout/delivery page')
    def enter_billing_address(self):
        fake = Faker('en_GB')
        street = fake.street_name()
        number = fake.building_number()
        post_code = fake.postcode()
        city = fake.city()
        self.enter_billing_address_street(street)
        self.enter_billing_address_number(number)
        self.enter_billing_address_post_code(post_code)
        self.enter_billing_address_city(city)

    # ASSERTIONS
    @allure.step('Assert the consent modal opens when clicking on the relevant link')
    def assert_consent_modal_opens(self):
        assert self.is_element_present(CheckoutDeliveryPageLocators.CONSENT_MODAL, timeout=3), \
            'Consent modal is not open'
        print('Consent modal is open')

    @allure.step('Assert Consent modal can be closed using the Close icon')
    def assert_consent_modal_closed(self):
        assert self.is_disappeared(CheckoutDeliveryPageLocators.CONSENT_MODAL), \
            'Consent modal is not closed'
        print('Consent modal closed')

    @allure.step('Assert the title is present in the consent modal')
    def assert_consent_modal_title_is_present(self):
        assert self.is_element_present(CheckoutDeliveryPageLocators.CONSENT_MODAL_TITLE, timeout=1), \
            'Consent modal title is missing'
        print('Consent modal title is present')
