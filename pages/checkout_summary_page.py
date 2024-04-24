import allure
from .base_page import BasePage
from locators import CheckoutSummaryPageLocators


class CheckoutSummaryPage(BasePage):
    # GETTERS
    def get_product_name_text(self):
        return self.find_element(CheckoutSummaryPageLocators.PRODUCT_NAME).text

    def get_product_color_text(self):
        return self.find_element(CheckoutSummaryPageLocators.PRODUCT_COLOR).text

    def get_product_price_value(self):
        return int(self.find_element(CheckoutSummaryPageLocators.PRODUCT_PRICE).text.split()[1].split('.')[0])

    def get_total_price_value(self):
        return int(self.find_element(CheckoutSummaryPageLocators.TOTAL_PRICE).text.split()[1].split('.')[0])

    def get_billing_address_text(self):
        """Get the street and the building number string text"""
        return self.find_element(CheckoutSummaryPageLocators.BILLING_ADDRESS).text

    def get_billing_postal_code_text(self):
        """Get the postal code and city string text"""
        return self.find_element(CheckoutSummaryPageLocators.BILLING_POST_CODE).text

    def get_accept_consent_error(self):
        return self.find_element(CheckoutSummaryPageLocators.ACCEPT_CONSENT_ERROR).text

    def get_css_accept_terms_checkbox_color_value(self):
        """Get css value for the border color of accept terms checkbox"""
        return self.find_element(CheckoutSummaryPageLocators.ACCEPT_TERMS_CHECKBOX)\
            .value_of_css_property('border-color')

    def get_consent_modal_title_text(self):
        """Get the title text in the terms modal"""
        return self.find_element(CheckoutSummaryPageLocators.CONSENT_MODAL_TITLE).text

    # ACTIONS
    @allure.step('Click Terms and Conditions link')
    def click_terms_and_conditions_link(self):
        self.find_element(CheckoutSummaryPageLocators.TERMS_AND_CONDITIONS_LINK).click()
        print('Click Terms and Conditions link')

    @allure.step('Click Accept Privacy Policy link')
    def click_accept_privacy_policy_link(self):
        self.find_element(CheckoutSummaryPageLocators.ACCEPT_PRIVACY_POLICY_LINK).click()
        print('Click Accept Privacy Policy link')

    @allure.step('Click Close icon in the Terms and Conditions or Accept Privacy Policy modal')
    def click_close_consent_modal_icon(self):
        self.find_element(CheckoutSummaryPageLocators.CLOSE_CONSENT_MODAL_ICON).click()
        print('Click Close icon in the Terms and Conditions or Accept Privacy Policy modal')

    @allure.step('Click Go Payments Details button')
    def click_go_to_payments_details_button(self):
        self.find_element(CheckoutSummaryPageLocators.GO_TO_PAYMENT_BTN).click()
        print('Click Go Payments Details button')

    @allure.step('Click Change billing address link')
    def click_change_billing_address_link(self):
        self.find_elements(CheckoutSummaryPageLocators.CHANGE_ADDRESS_LINK)[0].click()
        print('Click Change billing address link')

    # ASSERTIONS
    @allure.step('Assert the consent modal opens when clicking on the relevant link')
    def assert_consent_modal_opens(self):
        assert self.is_element_present(CheckoutSummaryPageLocators.CONSENT_MODAL, timeout=3), \
            'Consent modal is not open'
        print('Consent modal is open')

    @allure.step('Assert Consent modal can be closed using the Close icon')
    def assert_consent_modal_closed(self):
        assert self.is_disappeared(CheckoutSummaryPageLocators.CONSENT_MODAL), \
            'Consent modal is not closed'
        print('Consent modal closed')

    @allure.step('Assert the title is present in the consent modal')
    def assert_consent_modal_title_is_present(self):
        assert self.is_element_present(CheckoutSummaryPageLocators.CONSENT_MODAL_TITLE, timeout=1), \
            'Consent modal title is missing'
        print('Consent modal title is present')
