import allure
from .base_page import BasePage
from locators import CheckoutSummaryPageLocators


class CheckoutSummaryPage(BasePage):
    # GETTERS
    def get_product_name_text(self):
        return self.find_element(CheckoutSummaryPageLocators.PRODUCT_NAME).text

    def get_product_color_text(self):
        return self.find_element(CheckoutSummaryPageLocators.PRODUCT_COLOR).text

    def get_product_size_text(self):
        return self.find_element(CheckoutSummaryPageLocators.PRODUCT_SIZE).text

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

    # ACTIONS
    @allure.step('Select the card payment method')
    def select_card_payment_method(self):
        self.find_element(CheckoutSummaryPageLocators.CARD_PAYMENT_METHOD).click()
        print('Select the card payment method')

    @allure.step('Click Go Payments Details button')
    def click_go_to_payments_details_button(self):
        self.find_element(CheckoutSummaryPageLocators.GO_TO_PAYMENT_BTN).click()
        print('Click Go Payments Details button')

    @allure.step('Click Change billing address link')
    def click_change_billing_address_link(self):
        self.find_elements(CheckoutSummaryPageLocators.CHANGE_ADDRESS_LINK)[0].click()
        print('Click Change billing address link')
