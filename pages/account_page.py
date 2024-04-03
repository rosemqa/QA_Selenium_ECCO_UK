import random
import allure
from constants import AccountAlerts
from locators import AccountPageLocators
from .base_page import BasePage
from pytest_check import check


class AccountPage(BasePage):
    # GETTERS
    def get_greeting_title_text(self):
        return self.find_element(AccountPageLocators.GREETING_TITLE).text

    def get_user_name_text(self):
        """Get username on the Personal details page"""
        return self.select_random_year()

    def get_first_name_text(self):
        """Get first name on the EDIT page"""
        return self.find_element(AccountPageLocators.FIRST_NAME_FIELD).get_attribute('value')

    def get_last_name_text(self):
        """Get last name on the EDIT page"""
        return self.find_element(AccountPageLocators.LAST_NAME_FIELD).get_attribute('value')

    def get_phone_number_value(self):
        return self.find_element(AccountPageLocators.PHONE_NUMBER_FIELD).get_attribute('value')

    def get_date_picker_day_value(self):
        return self.find_element(AccountPageLocators.DAY_PICKER).text.lstrip('0')

    def get_date_picker_month_value(self):
        return self.find_element(AccountPageLocators.MONTH_PICKER).text.lstrip('0')

    def get_date_picker_year_value(self):
        return self.find_element(AccountPageLocators.YEAR_PICKER).text

    def get_day_to_choose_in_days_dropdown(self):
        """Get the value of the selected day in the year dropdown"""
        return str(self.random_day + 1)

    def get_month_to_choose_in_months_dropdown(self):
        """Get the value of the selected month in the month dropdown"""
        return str(self.random_month + 1)

    def get_year_to_choose_in_years_dropdown(self):
        """Get the value of the selected year in the year dropdown"""
        self.find_element(AccountPageLocators.YEAR_PICKER).click()
        year_value = self.find_element(AccountPageLocators.YEAR_TO_CHOOSE_SELECTED).text
        self.find_element(AccountPageLocators.YEAR_PICKER_CLOSE_ICON).click()
        return year_value

    def get_first_name_alert_text(self):
        return self.find_element(AccountPageLocators.FIRST_NAME_ERROR).text

    def get_last_name_alert_text(self):
        return self.find_element(AccountPageLocators.LAST_NAME_ERROR).text

    def get_email_alert_text(self):
        return self.find_element(AccountPageLocators.EMAIL_ERROR).text

    def get_phone_number_alert_text(self):
        return self.find_element(AccountPageLocators.PHONE_NUMBER_ERROR).text

    def get_updated_user_info_text(self):
        """Text appears for a few seconds when clicking the Save user info button"""
        return self.find_element(AccountPageLocators.UPDATED_USER_INFO_TEXT).text

    def get_favourites_page_title_text(self):
        return self.find_element(AccountPageLocators.MY_FAVOURITES_TITLE).text

    def get_favourites_product_name_text(self):
        return self.find_element(AccountPageLocators.PRODUCT_NAME).text

    def get_favourites_product_color_text(self):
        return self.find_element(AccountPageLocators.PRODUCT_COLOR).text

    def get_favourites_product_price_value(self):
        return int(self.find_element(AccountPageLocators.PRODUCT_PRICE).text.split()[1].split('.')[0])

    def get_empty_favourites_message_text(self):
        return self.find_element(AccountPageLocators.EMPTY_FAVORITES_MSG).text

    def get_share_link_text(self):
        """Get share link value on the favourites page"""
        return self.find_element(AccountPageLocators.COPY_LINK_FIELD).get_attribute('value')

    def get_address_book_street_text(self):
        """Get the street name value and house number on the address book page"""
        return self.find_element(AccountPageLocators.ADDRESS_BOOK_STREET).text

    def get_address_book_city_text(self):
        """Get the post code value and city name on the address book page"""
        return self.find_element(AccountPageLocators.ADDRESS_BOOK_CITY).text

    def get_address_book_no_address_text(self):
        """Get a message text saying the address is not specified"""
        return self.find_element(AccountPageLocators.NO_ADDRESS_MSG).text

    def get_street_alert_text(self):
        return self.find_element(AccountPageLocators.STREET_ERROR).text

    def get_house_number_alert_text(self):
        return self.find_element(AccountPageLocators.HOUSE_NUMBER_ERROR).text

    def get_post_code_error_text(self):
        return self.find_element(AccountPageLocators.POST_CODE_ERROR).text

    def get_city_error_text(self):
        return self.find_element(AccountPageLocators.CITY_ERROR).text

    def get_css_street_field_border_color_value(self):
        """Get css value for the border color of the street field"""
        return self.find_element(AccountPageLocators.BILLING_ADDRESS_STREET_FIELD).value_of_css_property('border-color')

    def get_css_number_field_border_color_value(self):
        """Get css value for the border color of the house number field"""
        return self.find_element(AccountPageLocators.BILLING_ADDRESS_NUMBER_FIELD).value_of_css_property('border-color')

    def get_css_postal_code_field_border_color_value(self):
        """Get css value for the border color of the postal code field"""
        return self.find_element(AccountPageLocators.BILLING_ADDRESS_POST_CODE_FIELD) \
            .value_of_css_property('border-color')

    def get_css_city_field_border_color_value(self):
        """Get css value for the border color of the city field"""
        return self.find_element(AccountPageLocators.BILLING_ADDRESS_CITY_FIELD).value_of_css_property('border-color')

    # ACTIONS
    @allure.step('Click See Details link')
    def click_see_details_link(self):
        self.find_element(AccountPageLocators.SEE_DETAILS_LINK).click()
        print('Click See Details link')

    @allure.step('Click See Orders link')
    def click_see_orders_link(self):
        self.find_element(AccountPageLocators.SEE_ORDERS_LINK).click()
        print('Click See Orders link')

    @allure.step('Click "Go to my favorites" link')
    def click_go_to_my_favorites_link(self):
        self.find_element(AccountPageLocators.GO_TO_MY_FAVORITES_LINK).click()
        print('Click "Go to my favorites" link')

    @allure.step('Click See Subscriptions link')
    def click_see_subscriptions_link(self):
        self.find_element(AccountPageLocators.SEE_SUBSCRIPTIONS_LINK).click()
        print('Click See Subscriptions link')

    @allure.step('Click SELECT MY STORE link')
    def click_select_my_store_link(self):
        self.find_element(AccountPageLocators.SELECT_MY_STORE_LINK).click()
        print('Click SELECT MY STORE link')

    @allure.step('Click Sigh Out button')
    def click_sign_out_button(self):
        self.find_element(AccountPageLocators.SIGH_OUT_BTN).click()
        print('Click Sigh Out button')

    @allure.step('Click "To My ECCO" link in the side menu')
    def click_to_my_ecco_link(self):
        self.find_element(AccountPageLocators.TO_MY_ECCO_LINK).click()
        print('Click "To My ECCO" link')

    @allure.step('Click "My Personal Details" link in the side menu')
    def click_my_personal_details_link(self):
        self.find_element(AccountPageLocators.MY_PERSONAL_DETAILS_LINK).click()
        print('Click "My Personal Details" link')

    @allure.step('Click "My Orders" link in the side menu')
    def click_my_orders_link(self):
        self.find_element(AccountPageLocators.MY_ORDERS_LINK).click()
        print('Click "My Orders" link')

    @allure.step('Click "My Favourites" link in the side menu')
    def click_my_favourites_link(self):
        self.find_element(AccountPageLocators.MY_FAVOURITES_LINK).click()
        print('Click "My Favourites" link')

    @allure.step('Click "My Subscriptions" link in the side menu')
    def click_my_subscriptions_link(self):
        self.find_element(AccountPageLocators.MY_SUBSCRIPTIONS_LINK).click()
        print('Click "My Subscriptions" link')

    @allure.step('Enter first name on the Edit page')
    def enter_first_name(self, first_name):
        self.find_element(AccountPageLocators.FIRST_NAME_FIELD).send_keys(first_name)
        print('Enter first name')

    @allure.step('Clear first name field on the Edit page')
    def clear_first_name_field(self):
        self.find_element(AccountPageLocators.FIRST_NAME_FIELD).clear()
        print('Clear first name field')

    @allure.step('Enter last name on the Edit page')
    def enter_last_name(self, last_name):
        self.find_element(AccountPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        print('Enter last name')

    @allure.step('Clear last name field on the Edit page')
    def clear_last_name_field(self):
        self.find_element(AccountPageLocators.LAST_NAME_FIELD).clear()
        print('Clear last name field')

    @allure.step('Enter email on the Edit page')
    def enter_email(self, email):
        self.find_element(AccountPageLocators.EMAIL_FIELD).send_keys(email)
        print('Enter email')

    @allure.step('Clear email field on the Edit page')
    def clear_email_field(self):
        self.find_element(AccountPageLocators.EMAIL_FIELD).clear()
        print('Clear email field')

    @allure.step('Enter phone number on the Edit page')
    def enter_phone_number(self, phone_number):
        self.find_element(AccountPageLocators.PHONE_NUMBER_FIELD).send_keys(phone_number)
        print('Enter phone number')

    @allure.step('Clear phone number field on the Edit page')
    def clear_phone_number_field(self):
        self.find_element(AccountPageLocators.PHONE_NUMBER_FIELD).clear()
        print('Clear phone number field')

    @allure.step('Click day picker ("dd")')
    def click_day_picker(self):
        self.find_element(AccountPageLocators.DAY_PICKER).click()
        print('Click day picker')

    @allure.step('Click month picker ("mm")')
    def click_month_picker(self):
        self.find_element(AccountPageLocators.MONTH_PICKER).click()
        print('Click month picker')

    @allure.step('Click year picker ("yyyy")')
    def click_year_picker(self):
        self.find_element(AccountPageLocators.YEAR_PICKER).click()
        print('Click year picker')

    @allure.step('Select random day (from 01 to 28)')
    def select_random_day(self):
        self.random_day = random.randint(0, 27)
        self.find_elements(AccountPageLocators.DAY_TO_CHOOSE)[self.random_day].click()
        print('Select random day')

    @allure.step('Select random month (from 1 to 12)')
    def select_random_month(self):
        self.random_month = random.randint(0, 11)
        self.find_elements(AccountPageLocators.MONTH_TO_CHOOSE)[self.random_month].click()
        print('Select random month')

    @allure.step('Select random year')
    def select_random_year(self):
        random_year = random.randint(0, 108)
        self.find_elements(AccountPageLocators.YEAR_TO_CHOOSE)[random_year].click()
        print('Select random year')

    @allure.step('Click the underlined "Clear" link')
    def click_clear_link(self):
        self.find_element(AccountPageLocators.CLEAR_DATE_LINK).click()
        print('Click Clear link')

    @allure.step('Click Save user details button')
    def click_save_user_details_button(self):
        self.find_element(AccountPageLocators.SAVE_USER_DETAILS_BTN).click()
        print('Click Save user details button')

    @allure.step('Click "Delete favourite" button')
    def click_delete_favourite_button(self):
        self.find_element(AccountPageLocators.DELETE_FAVOURITE_BTN).click()
        print('Click "Delete favourite" button')

    @allure.step('Click OK button in the modal when deleting from favorites')
    def confirm_deletion_in_the_modal(self):
        self.find_element(AccountPageLocators.DELETE_FAVOURITE_OK_BUTTON).click()
        print('Confirm deletion in the modal')

    @allure.step('Click "Share you favourites" button')
    def click_share_favourites_button(self):
        self.find_element(AccountPageLocators.SHARE_FAVOURITES_BTN).click()
        print('Click "Share you favourites" button')

    @allure.description('Click the product title in Favourites')
    def click_favourite_product_name(self):
        self.find_element(AccountPageLocators.PRODUCT_NAME).click()
        print('Click favourite product name')

    @allure.step('Click Add Address button')
    def click_add_address_button(self):
        self.find_element(AccountPageLocators.ADD_ADDRESS_BTN).click()
        print('Click Add Address button')

    @allure.step('Click Edit Address link on the Address Book page')
    def click_edit_address_link(self):
        self.find_element(AccountPageLocators.EDIT_ADDRESS_LINK).click()
        print('Click Edit Address link')

    @allure.step('Click Delete button on the Address Book page')
    def click_delete_address_button(self):
        self.find_element(AccountPageLocators.DELETE_ADDRESS_BTN).click()
        print('Click Delete address button')

    @allure.step('Click OK button in the modal when deleting the address')
    def confirm_address_deletion(self):
        self.find_element(AccountPageLocators.DELETE_ADDRESS_OK_BUTTON).click()
        print('Confirm address deletion')

    @allure.step('Enter the billing address street')
    def enter_billing_address_street(self, street):
        self.find_element(AccountPageLocators.BILLING_ADDRESS_STREET_FIELD).send_keys(street)
        print('Enter billing address street')

    @allure.step('Enter the billing address house number')
    def enter_billing_address_number(self, number):
        self.find_element(AccountPageLocators.BILLING_ADDRESS_NUMBER_FIELD).send_keys(number)
        print('Enter billing address house number')

    @allure.step('Enter the billing address post code')
    def enter_billing_address_post_code(self, post_code):
        self.find_element(AccountPageLocators.BILLING_ADDRESS_POST_CODE_FIELD).send_keys(post_code)
        print('Enter billing address post code')

    @allure.step('Enter the billing address city')
    def enter_billing_address_city(self, city):
        self.find_element(AccountPageLocators.BILLING_ADDRESS_CITY_FIELD).send_keys(city)
        print('Enter billing address city')

    @allure.step('Click Save billing address button')
    def click_save_billing_address_button(self):
        self.find_element(AccountPageLocators.BILLING_ADDRESS_SAVE_BTN).click()
        print('Click Save billing address button')

    @allure.step('Clear the billing address Street field')
    def clear_billing_address_street(self):
        self.find_element(AccountPageLocators.BILLING_ADDRESS_STREET_FIELD).clear()
        print('Clear the billing address Street field')

    @allure.step('Clear the billing address Number field')
    def clear_billing_address_house_number(self):
        self.find_element(AccountPageLocators.BILLING_ADDRESS_NUMBER_FIELD).clear()
        print('Clear the billing address Number field')

    @allure.step('Clear the billing address Post Code field')
    def clear_billing_address_post_code(self):
        self.find_element(AccountPageLocators.BILLING_ADDRESS_POST_CODE_FIELD).clear()
        print('Clear the billing address Post Code field')

    @allure.step('Clear the billing address City field')
    def clear_billing_address_city(self):
        self.find_element(AccountPageLocators.BILLING_ADDRESS_CITY_FIELD).clear()
        print('Clear the billing address City field')

    # ASSERTIONS
    @allure.step('Assert the greeting title is present when logging in')
    def assert_greeting_title_is_present(self):
        assert self.is_element_present(AccountPageLocators.GREETING_TITLE), \
            'Greeting title is missing'
        print('Greeting title is present')

    @allure.step('Assert updated user info message disappears after 6 seconds')
    def assert_updated_info_msg_disappears(self):
        assert self.is_disappeared(AccountPageLocators.UPDATED_USER_INFO_TEXT, timeout=6), \
            'Updated user info message does not disappear after 6 seconds'
        print('Updated user info message disappears')

    @allure.step('Assert "Sign in now" button is present for a non-logged in user')
    def assert_sign_in_button_is_present(self):
        assert self.is_element_present(AccountPageLocators.SIGN_IN_BTN), \
            'Sign In Now button is missing'
        print('"Sign in now" button is present')

    def assert_no_billing_address(self):
        with check:
            assert self.is_element_present(AccountPageLocators.ADD_ADDRESS_BTN), \
                'Add Address button is missing, probably the address is not deleted'
        with check:
            assert self.get_address_book_no_address_text() == AccountAlerts.NO_BILLING_ADDRESS_MESSAGE, \
                f'No billing address message text is not correct,' \
                f' expected: { AccountAlerts.NO_BILLING_ADDRESS_MESSAGE}, ' \
                f'actual: {self.get_address_book_no_address_text()}'
