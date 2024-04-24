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
