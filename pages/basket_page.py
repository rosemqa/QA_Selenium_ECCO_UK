import allure
from .base_page import BasePage
from locators import BasketPageLocators


class BasketPage(BasePage):
    # GETTERS
    def get_product_name_text(self):
        return self.find_element(BasketPageLocators.PRODUCT_NAME).text

    def get_product_color_text(self):
        return self.find_element(BasketPageLocators.PRODUCT_COLOR).text

    def get_product_size_text(self):
        return self.find_element(BasketPageLocators.PRODUCT_SIZE).text

    def get_product_price_value(self):
        return int(self.find_element(BasketPageLocators.PRODUCT_PRICE).text.split()[1].split('.')[0])

    def get_total_price_value(self):
        return int(self.find_element(BasketPageLocators.TOTAL_PRICE).text.split()[1].split('.')[0])

    def get_choose_store_button_text(self):
        """Get text in the Choose Store button in the Click & Collect section"""
        return self.find_element(BasketPageLocators.CHOOSE_STORE_BTN).text

    def get_pickup_store_name_text(self):
        """Get the store name in the Click & Collect section"""
        return self.find_element(BasketPageLocators.STORE_NAME).text

    def get_modal_pickup_store_name(self):
        """Get the store name in the store locator modal"""
        return self.find_element(BasketPageLocators.STORE_LOCATOR_STORE_NAME).text

    def get_voucher_code_error(self):
        return self.find_element(BasketPageLocators.VOUCHER_CODE_ERROR).text

    def get_empty_basket_message_text(self):
        return self.find_element(BasketPageLocators.EMPTY_BASKET_MSG).text

    # ACTIONS
    @allure.step('Click lower Checkout Now button')
    def click_lower_checkout_button(self):
        self.find_element(BasketPageLocators.LOWER_CHECKOUT_BTN).click()
        print('Click lower Checkout Now button')

    @allure.step('Click Remove button')
    def click_remove_button(self):
        self.find_element(BasketPageLocators.DELETE_BTN).click()
        print('Click Remove button')

    @allure.step('Enter the voucher code')
    def enter_voucher_code(self, code):
        self.find_element(BasketPageLocators.VOUCHER_CODE_FIELD).send_keys(code)
        print('Enter the voucher code')

    @allure.step('Click the Redeem code button')
    def click_redeem_button(self):
        self.find_element(BasketPageLocators.REDEEM_CODE).click()
        print('Click the Redeem code button')

    @allure.step('Select the Clik & Collect delivery method')
    def select_click_and_collect_delivery(self):
        self.find_element(BasketPageLocators.CLICK_AND_COLLECT_RADIO_BTN).click()
        print('Select the Clik & Collect delivery method')

    @allure.step('Click the Choose/Change store button')
    def click_choose_store_button(self):
        self.find_element(BasketPageLocators.CHOOSE_STORE_BTN).click()
        print('Click the Choose/Change store button')

    @allure.step('Click the Select store button in the store locator modal')
    def click_select_store_button_in_modal(self):
        self.find_element(BasketPageLocators.SELECT_STORE_BTN).click()
        print('Click the Select store button in the store locator modal')

    @allure.step('Click the Continue Shopping button in the empty basket')
    def click_continue_shopping_button(self):
        self.find_element(BasketPageLocators.CONTINUE_SHOPPING_BTN).click()
        print('Click the Continue Shopping button in the empty basket')

    @allure.step('Click the product title')
    def click_product_title(self):
        self.find_element(BasketPageLocators.PRODUCT_NAME).click()
        print('Click the product title')

    # ASSERTIONS
    @allure.step('Assert the Continue Shopping button is present in the the empty basket')
    def assert_continue_shopping_button_is_present(self):
        assert self.is_element_present(BasketPageLocators.CONTINUE_SHOPPING_BTN), \
            'Continue Shopping button is missing in the empty basket, probably a product is not deleted'
        print('Continue Shopping button is present')
