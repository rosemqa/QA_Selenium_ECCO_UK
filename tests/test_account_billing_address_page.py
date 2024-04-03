import allure
from faker import Faker
from pages.account_page import AccountPage
from constants import URL, AccountAlerts


@allure.epic('Account > billing address cases')
class TestBillingAddress:
    @allure.description('Test that user can add the new billing address')
    def test_add_new_billing_address(self, check, driver, login, delete_billing_address):
        faker = Faker('en_GB')
        street = faker.street_name()
        house_number = faker.building_number()
        post_code = faker.postcode()
        city = faker.city()

        page = AccountPage(driver, URL.BILLING_ADDRESS_BOOK_PAGE)
        page.open_page()
        page.click_add_address_button()

        page.enter_billing_address_street(street)
        page.enter_billing_address_number(house_number)
        page.enter_billing_address_post_code(post_code)
        page.enter_billing_address_city(city)
        page.click_save_billing_address_button()

        assert page.get_current_url() == URL.BILLING_ADDRESS_BOOK_PAGE, \
            'User is not redirected to Address Book page after saving the new address'
        address_book_street = page.get_address_book_street_text()
        address_book_city = page.get_address_book_city_text()
        with check:
            assert address_book_street == f'{street} {house_number}', \
                'Street or house number on the Address Book page do not match the entered values on the Address page'
        with check:
            assert address_book_city == f'{post_code} {city}', \
                'Post code or city on the Address Book page do not match the entered values on the Address page'

    @allure.description('Check the error messages and the field border color when saving address with empty fields')
    @allure.tag('negative')
    def test_add_address_with_empty_fields(self, check, driver, login):
        input_field_border_color = 'rgb(218, 68, 50)'

        page = AccountPage(driver, URL.EDIT_BILLING_ADDRESS_PAGE)
        page.open_page()
        page.click_save_billing_address_button()

        with check:
            assert page.get_street_alert_text() == AccountAlerts.ADDRESS_EMPTY_STREET_ALERT, \
                'Empty street alert text is not correct'
        with check:
            assert page.get_house_number_alert_text() == AccountAlerts.ADDRESS_EMPTY_NUMBER_ALERT, \
                'Empty house number alert text is not correct'
        with check:
            assert page.get_post_code_error_text() == AccountAlerts.ADDRESS_EMPTY_CODE_ALERT, \
                'Empty post_code alert text is not correct'
        with check:
            assert page.get_city_error_text() == AccountAlerts.ADDRESS_EMPTY_CITY_ALERT, \
                'Empty city alert text is not correct'
        assert page.get_css_street_field_border_color_value() == input_field_border_color, \
            'Street field border color is not correct'
        assert page.get_css_number_field_border_color_value() == input_field_border_color, \
            'House number field border color is not correct'
        assert page.get_css_postal_code_field_border_color_value() == input_field_border_color, \
            'Postal code field border color is not correct'
        assert page.get_css_city_field_border_color_value() == input_field_border_color, \
            'City field border color is not correct'

    @allure.description('Test that the billing address can be edited')
    def test_edit_billing_address(self, check, driver, login, add_billing_address, delete_billing_address):
        faker = Faker('en_GB')
        street = faker.street_name()
        house_number = faker.building_number()
        post_code = faker.postcode()
        city = faker.city()

        page = AccountPage(driver, URL.BILLING_ADDRESS_BOOK_PAGE)

        page.click_edit_address_link()
        page.clear_billing_address_street()
        page.clear_billing_address_house_number()
        page.clear_billing_address_post_code()
        page.clear_billing_address_city()
        page.enter_billing_address_street(street)
        page.enter_billing_address_number(house_number)
        page.enter_billing_address_post_code(post_code)
        page.enter_billing_address_city(city)
        page.click_save_billing_address_button()

        assert page.get_current_url() == URL.BILLING_ADDRESS_BOOK_PAGE, \
            'User is not redirected to Address Book page after saving the new address'
        address_book_street = page.get_address_book_street_text()
        address_book_city = page.get_address_book_city_text()
        with check:
            assert address_book_street == f'{street} {house_number}', \
                'Street or house number on the Address Book page do not match the entered values on the Address page'
        with check:
            assert address_book_city == f'{post_code} {city}', \
                'Post code or city on the Address Book page do not match the entered values on the Address page'

    @allure.description('Test that the billing address can be deleted')
    def test_delete_billing_address(self, driver, login, add_billing_address):
        page = AccountPage(driver, URL.BILLING_ADDRESS_BOOK_PAGE)

        page.click_delete_address_button()
        page.confirm_address_deletion()

        page.assert_no_billing_address()
